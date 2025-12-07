from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

# Правильные импорты даты и времени
from datetime import date, time, datetime, timedelta
from django.utils import timezone

# Модели и формы
from .models import Patient, Doctor, Appointment, Service, ServiceCategory, AppointmentDocument
from .forms import PatientAppointmentForm, PatientUserForm, PatientForm, PatientUserUpdateForm, SimpleAppointmentForm, UploadDocumentsForm
from .decorators import is_patient, is_doctor


def home_view(request):
    """
    Главная страница с услугами, сгруппированными по категориям.
    """
    categories = ServiceCategory.objects.prefetch_related('service_set').all()
    doctors = Doctor.objects.filter(status=True)  # Добавляем врачей
    context = {
        'categories': categories,
        'doctors': doctors
    }
    return render(request, 'clinic/index.html', context)


def doctors_view(request):
    """
    Страница с информацией о всех врачах.
    """
    doctors = Doctor.objects.filter(status=True)
    return render(request, 'clinic/doctors.html', {'doctors': doctors})


@login_required(login_url='login')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient = Patient.objects.get(user_id=request.user.id)
    visitDate = patient.first_visit_date

    next_appointment = Appointment.objects.filter(
        patient=patient,
        appointment_date__gte=timezone.now(),
        status=True
    ).order_by('appointment_date').first()

    context = {
        'patient': patient,
        'visitDate': visitDate,
        'next_appointment': next_appointment,
    }
    return render(request, 'clinic/patient_dashboard.html', context)


@login_required(login_url='login')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    doctor = Doctor.objects.get(user_id=request.user.id)
    appointments = Appointment.objects.filter(dentist=doctor).order_by('appointment_date')
    today = date.today()

    today_appointments = appointments.filter(appointment_date__date=today)
    future_appointments = appointments.filter(appointment_date__date__gt=today)
    past_appointments = appointments.filter(appointment_date__date__lt=today)

    context = {
        'doctor': doctor,
        'today_appointments': today_appointments,
        'future_appointments': future_appointments,
        'past_appointments': past_appointments,
    }
    return render(request, 'clinic/doctor_dashboard.html', context)


@login_required(login_url='login')
@user_passes_test(is_doctor)
def doctor_appointment_detail_view(request, appointment_id):
    doctor = Doctor.objects.get(user_id=request.user.id)
    appointment = Appointment.objects.get(id=appointment_id, dentist=doctor)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'confirm':
            appointment.is_attended = True
            appointment.save()
            messages.success(request, 'Приём подтверждён.')
        elif action == 'cancel':
            appointment.is_attended = False
            appointment.save()
            messages.info(request, 'Пациент не пришёл.')
        elif action == 'reschedule':
            new_date = request.POST.get('new_date')
            new_time = request.POST.get('new_time')
            if new_date and new_time:
                try:
                    new_datetime_str = f"{new_date}T{new_time}"
                    new_datetime = datetime.fromisoformat(new_datetime_str)
                    if is_working_day(new_datetime.date()) and not Appointment.objects.filter(
                            appointment_date=new_datetime, status=True, dentist=doctor
                    ).exists():
                        appointment.appointment_date = new_datetime
                        appointment.save()
                        messages.success(request, f'Визит перенесён на {new_datetime.strftime("%d.%m.%Y в %H:%M")}.')
                    else:
                        messages.error(request, 'Выбранное время недоступно.')
                except Exception as e:
                    messages.error(request, f'Некорректная дата или время: {str(e)}')
            else:
                messages.error(request, 'Укажите новую дату и время.')

        # Сохранение комментария
        comment = request.POST.get('comment', '').strip()
        appointment.comment = comment
        appointment.save()

        # Загрузка документов (до 5)
        files = request.FILES.getlist('files')
        existing_count = appointment.documents.count()
        for uploaded_file in files:
            if existing_count >= 5:
                messages.warning(request, 'Можно загрузить не более 5 документов.')
                break
            AppointmentDocument.objects.create(
                appointment=appointment,
                file=uploaded_file
            )
            existing_count += 1

        messages.success(request, 'Данные приёма обновлены.')
        return redirect('doctor-appointment-detail', appointment_id=appointment.id)

    past_appointments = Appointment.objects.filter(
        patient=appointment.patient,
        appointment_date__lt=timezone.now(),
        status=True
    ).order_by('-appointment_date')

    context = {
        'appointment': appointment,
        'past_appointments': past_appointments,
        'is_today': appointment.appointment_date.date() == timezone.now().date(),
    }
    return render(request, 'clinic/doctor_appointment_detail.html', context)


def service_list_view(request):
    category_id = request.GET.get('category')
    categories = ServiceCategory.objects.prefetch_related('service_set').all()

    if category_id:
        try:
            selected_category = ServiceCategory.objects.get(id=category_id)
            services = selected_category.service_set.all()
            categories = [selected_category]
        except ServiceCategory.DoesNotExist:
            services = Service.objects.none()
    else:
        selected_category = None
        services = Service.objects.all()

    return render(request, 'clinic/service_list.html', {
        'categories': categories,
        'services': services,
        'selected_category': selected_category
    })


def is_working_day(check_date):
    """
    Проверяет, является ли дата рабочим днём (по производственному календарю РФ на 2025–2026 годы).
    """
    if check_date.weekday() >= 5:  # Сб = 5, Вс = 6
        return False

    holidays = [
        # 2025 год
        '2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05', '2025-01-06',
        '2025-01-07', '2025-01-08', '2025-02-24', '2025-03-10', '2025-05-01', '2025-05-09',
        '2025-05-12', '2025-06-12', '2025-11-03', '2025-11-04',
        # 2026 год
        '2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05', '2026-01-06',
        '2026-01-07', '2026-01-08', '2026-02-23', '2026-03-09', '2026-05-01', '2026-05-11',
        '2026-06-12', '2026-11-02', '2026-11-03'
    ]
    return str(check_date) not in holidays


def is_time_in_range(appointment_time):
    """
    Проверяет, входит ли время в диапазон с 8:00 до 20:00.
    """
    start_time = time(8, 0)
    end_time = time(20, 0)
    return start_time <= appointment_time <= end_time


def is_time_slot_available(appointment_datetime, dentist, exclude_appointment_id=None):
    """
    Проверяет, доступен ли слот (интервал 60 минут) для записи.
    """
    # Проверка на занятость другим приёмом
    query = Appointment.objects.filter(
        appointment_date=appointment_datetime,
        dentist=dentist,
        status=True
    )
    if exclude_appointment_id:
        query = query.exclude(id=exclude_appointment_id)

    return not query.exists()


@login_required(login_url='login')
@user_passes_test(is_patient)
def patient_appointment_view(request):
    patient = Patient.objects.get(user_id=request.user.id)
    appointments = Appointment.objects.filter(patient=patient, status=True)
    context = {
        'appointments': appointments,
        'patient': patient,
    }
    return render(request, 'clinic/patient_appointment.html', context)


@login_required(login_url='login')
@user_passes_test(is_patient)
def patient_book_appointment_view(request):
    doctors = Doctor.objects.filter(status=True)
    patient = Patient.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        dentist_id = request.POST.get('dentist')
        appointment_datetime_str = request.POST.get('appointment_datetime')  # Получаем из скрытого поля
        description = request.POST.get('description', '')

        if not dentist_id:
            messages.error(request, 'Пожалуйста, выберите врача.')
        elif not appointment_datetime_str:
            messages.error(request, 'Пожалуйста, выберите дату и время.')
        else:
            try:
                # Преобразуем строку в datetime
                naive_datetime = datetime.fromisoformat(appointment_datetime_str)
                appointment_datetime = timezone.make_aware(naive_datetime, timezone.get_current_timezone())

                # Проверки
                if not is_working_day(appointment_datetime.date()):
                    messages.error(request, 'Выбранная дата — выходной или праздник.')
                elif not is_time_in_range(appointment_datetime.time()):
                    messages.error(request, 'Время должно быть с 08:00 до 20:00.')
                elif not is_time_slot_available(appointment_datetime, Doctor.objects.get(id=dentist_id)):
                    messages.error(request, 'Это время уже занято. Выберите другое.')
                else:
                    # Создаём запись
                    appointment = Appointment(
                        patient=patient,
                        dentist=Doctor.objects.get(id=dentist_id),
                        appointment_date=appointment_datetime,
                        description=description,
                        status=True
                    )
                    appointment.save()
                    messages.success(request, f'Вы успешно записаны на {appointment_datetime.strftime("%d.%m.%Y в %H:%M")}.')
                    return redirect('patient-view-appointment')
            except Exception as e:
                messages.error(request, f'Ошибка при записи: {str(e)}')

    return render(request, 'clinic/patient_book_appointment.html', {
        'doctors': doctors
    })


@login_required(login_url='login')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient = Patient.objects.get(user_id=request.user.id)
    appointments = Appointment.objects.filter(patient=patient, status=True).order_by('-appointment_date')

    context = {
        'appointments': appointments,
        'now': timezone.now(),
    }
    return render(request, 'clinic/patient_view_appointment.html', context)


def contactus_view(request):
    return render(request, 'clinic/contact_us.html')


def aboutus_view(request):
    return render(request, 'clinic/aboutus.html')


def patient_signup_view(request):
    if request.method == 'POST':
        user_form = PatientUserForm(request.POST)
        patient_form = PatientForm(request.POST, request.FILES)
        print("Form is valid:", user_form.is_valid())  # Отладка
        print("Form errors:", user_form.errors)        # Что не так?
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient_group, created = Group.objects.get_or_create(name='PATIENT')
            user.groups.add(patient_group)
            user.save()

            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()

            # Автоматический вход после регистрации
            auth_login(request, user)

            messages.success(request, 'Регистрация успешна! Вы вошли в систему.')
            return redirect('patient-dashboard')
    else:
        user_form = PatientUserForm()
        patient_form = PatientForm()

    return render(request, 'clinic/patient_signup.html', {
        'user_form': user_form,
        'patient_form': patient_form
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            if user.groups.filter(name='PATIENT').exists():
                return redirect('patient-dashboard')
            elif user.groups.filter(name='DOCTOR').exists():
                return redirect('doctor-dashboard')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'clinic/login.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(is_patient)
def patient_edit_profile_view(request):
    patient = Patient.objects.get(user_id=request.user.id)
    user = patient.user

    if request.method == 'POST':
        user_form = PatientUserUpdateForm(request.POST, instance=user)
        patient_form = PatientForm(request.POST, request.FILES, instance=patient)

        if user_form.is_valid() and patient_form.is_valid():
            user_form.save()
            patient_form.save()
            messages.success(request, 'Ваш профиль успешно обновлён!')
            return redirect('patient-dashboard')
    else:
        user_form = PatientUserUpdateForm(instance=user)
        patient_form = PatientForm(instance=patient)

    context = {
        'user_form': user_form,
        'patient_form': patient_form
    }
    return render(request, 'clinic/patient_edit_profile.html', context)


def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()


@login_required(login_url='login')
@user_passes_test(is_doctor)
def patient_list_view(request):
    # Все пациенты, у которых были приёмы
    patients = Patient.objects.all().order_by('user__last_name', 'user__first_name')
    return render(request, 'clinic/patient_list.html', {'patients': patients})


@login_required(login_url='login')
@user_passes_test(is_patient)
def cancel_appointment_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient__user=request.user)

    if appointment.appointment_date <= timezone.now():
        messages.error(request, 'Нельзя отменить прошедший приём.')
    else:
        appointment.delete()
        messages.success(request, 'Запись успешно отменена.')

    return redirect('patient-view-appointment')


@login_required(login_url='login')
@user_passes_test(is_doctor)
def patient_detail_view(request, patient_id):
    # Доктор может посмотреть историю любого пациента
    patient = get_object_or_404(Patient, id=patient_id)
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')

    return render(request, 'clinic/patient_detail.html', {
        'patient': patient,
        'appointments': appointments
    })


@login_required(login_url='login')
@user_passes_test(is_patient)
def reschedule_appointment_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient__user=request.user)

    if appointment.appointment_date <= timezone.now():
        messages.error(request, 'Нельзя перенести прошедший приём.')
        return redirect('patient-view-appointment')

    # Генерация часов для шаблона (на случай, если JS отключён)
    available_hours = []
    for hour in range(8, 20):
        slot_time = time(hour, 0)
        slot_datetime = timezone.make_aware(
            datetime.combine(timezone.now().date(), slot_time),
            timezone.get_current_timezone()
        )
        if is_working_day(slot_datetime.date()) and is_time_in_range(slot_time):
            available_hours.append(slot_datetime)

    if request.method == 'POST':
        new_date = request.POST.get('new_date')
        new_time = request.POST.get('new_time')  # Получаем в формате "HH:MM"

        if not new_date or not new_time:
            messages.error(request, 'Укажите дату и время.')
        else:
            try:
                # Парсим время как часы:минуты
                hour, minute = map(int, new_time.split(':'))
                if minute != 0:
                    messages.error(request, 'Минуты должны быть 00. Выберите время из списка.')
                else:
                    naive_datetime = datetime.strptime(f"{new_date} {new_time}", "%Y-%m-%d %H:%M")
                    new_datetime = timezone.make_aware(naive_datetime, timezone.get_current_timezone())

                    appt_date = new_datetime.date()
                    appt_time = new_datetime.time()

                    if not is_working_day(appt_date):
                        messages.error(request, 'Можно перенести только на рабочий день (пн–пт, не праздник).')
                    elif not is_time_in_range(appt_time):
                        messages.error(request, 'Время должно быть с 08:00 до 20:00.')
                    elif not is_time_slot_available(new_datetime, appointment.dentist, exclude_appointment_id=appointment.id):
                        messages.error(request, 'Это время уже занято.')
                    else:
                        appointment.appointment_date = new_datetime
                        appointment.save()
                        messages.success(request, f'Запись перенесена на {new_datetime.strftime("%d.%m.%Y в %H:%M")}.')
                        return redirect('patient-view-appointment')
            except ValueError as ve:
                messages.error(request, 'Некорректный формат времени.')
            except Exception as e:
                messages.error(request, f'Ошибка при переносе: {str(e)}')

    return render(request, 'clinic/reschedule_appointment.html', {
        'appointment': appointment,
        'available_hours': available_hours
    })


@login_required(login_url='login')
@user_passes_test(is_doctor)
def doctor_reschedule_appointment_view(request, appointment_id):
    doctor = Doctor.objects.get(user_id=request.user.id)
    appointment = get_object_or_404(Appointment, id=appointment_id, dentist=doctor)

    if request.method == 'POST':
        new_date = request.POST.get('new_date')
        new_time = request.POST.get('new_time')

        if not new_date or not new_time:
            messages.error(request, 'Укажите дату и время.')
        else:
            try:
                naive_datetime = datetime.strptime(f"{new_date} {new_time}", "%Y-%m-%d %H:%M")
                new_datetime = timezone.make_aware(naive_datetime, timezone.get_current_timezone())

                if not is_working_day(new_datetime.date()):
                    messages.error(request, 'Выбранная дата недоступна.')
                elif Appointment.objects.filter(
                        appointment_date=new_datetime,
                        status=True,
                        dentist=doctor
                ).exclude(id=appointment_id).exists():
                    messages.error(request, 'Это время уже занято.')
                else:
                    appointment.appointment_date = new_datetime
                    appointment.save()
                    messages.success(request, f'Визит перенесён на {new_datetime.strftime("%d.%m.%Y в %H:%M")}.')
                    return redirect('doctor-appointment-detail', appointment_id=appointment.id)
            except ValueError as e:
                messages.error(request, 'Некорректный формат времени.')
            except Exception as e:
                messages.error(request, 'Ошибка при переносе.')

    return render(request, 'clinic/doctor_reschedule_appointment.html', {'appointment': appointment})


def get_available_slots_json(request):
    """
    Возвращает доступные слоты для врача на выбранную дату.
    Используется для динамической загрузки времени при выборе даты.
    """
    date_str = request.GET.get('date')
    doctor_id = request.GET.get('doctor_id')

    if not doctor_id or doctor_id == 'undefined':
        return JsonResponse({'slots': []})

    try:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        if not is_working_day(selected_date) or selected_date < timezone.now().date():
            return JsonResponse({'slots': []})

        # Генерируем слоты: 08:00, 09:00, ..., 19:00 (интервал 60 минут)
        start_hour = 8
        end_hour = 20
        slot_duration = timedelta(hours=1)

        slots = []
        current = datetime.combine(selected_date, time(start_hour, 0))
        end = datetime.combine(selected_date, time(end_hour, 0))

        while current < end:
            slots.append(current.time())
            current += slot_duration

        # Проверяем занятость
        booked_times = Appointment.objects.filter(
            appointment_date__date=selected_date,
            dentist_id=int(doctor_id),
            status=True
        ).values_list('appointment_date__time', flat=True)

        free_slots = [slot.strftime('%H:%M') for slot in slots if slot not in booked_times]

        return JsonResponse({'slots': free_slots})
    except Exception as e:
        print(f"Error in get_available_slots_json: {e}")
        return JsonResponse({'slots': []})