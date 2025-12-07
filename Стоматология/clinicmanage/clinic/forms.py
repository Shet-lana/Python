from django import forms
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment


class PatientUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтверждение пароля'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Логин',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Этот логин уже занят. Пожалуйста, выберите другой.")
        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")
        return password_confirm

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Пароль должен содержать не менее 8 символов.")
        if not any(c.isalpha() for c in password):
            raise forms.ValidationError("Пароль должен содержать хотя бы одну букву.")
        if not any(c.isdigit() for c in password):
            raise forms.ValidationError("Пароль должен содержать хотя бы одну цифру.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['address', 'mobile', 'profile_pic']
        labels = {
            'address': 'Адрес',
            'mobile': 'Телефон',
            'profile_pic': 'Фото профиля',
        }
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class AppointmentForm(forms.ModelForm):
    assigned_dentist = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(status=True),
        label='Врач',
        empty_label="Выберите врача"
    )
    patientId = forms.ModelChoiceField(
        queryset=Patient.objects.filter(status=True),
        label='Пациент',
        empty_label="Выберите пациента"
    )

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'description', 'status']
        labels = {
            'appointment_date': 'Дата приёма',
            'description': 'Описание',
            'status': 'Статус (подтверждён)',
        }
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PatientAppointmentForm(forms.ModelForm):
    dentist = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(status=True),
        label="Выберите врача",
        empty_label="--- Выберите врача ---",
        widget=forms.Select(attrs={
            'id': 'id_dentist',
            'name': 'dentist',
            'class': 'form-control'
        }),
    )

    class Meta:
        model = Appointment
        fields = ['dentist', 'appointment_date', 'description']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30, label='Ваше имя')
    Email = forms.EmailField(label='Электронная почта')
    Message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        label='Сообщение'
    )


class PatientUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Логин',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SimpleAppointmentForm(forms.ModelForm):
    dentist = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(status=True),
        label="Врач",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    appointment_date = forms.DateTimeField(
        label="Дата и время",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
    )
    description = forms.CharField(
        label="Жалобы",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )

    class Meta:
        model = Appointment
        fields = ['dentist', 'appointment_date', 'description']


class UploadDocumentsForm(forms.Form):
    files = forms.FileField(
        label='Загрузить файлы',
        help_text='Можно загрузить до 5 файлов',
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание (необязательно)'}),
    )