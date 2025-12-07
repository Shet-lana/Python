import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Doctor(models.Model):
    """Модель врача-стоматолога."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/doctor_profiles/', null=True, blank=True)
    about = models.TextField(max_length=500, blank=True, verbose_name="О враче")
    department = models.CharField(max_length=100, blank=True, verbose_name="Отделение")
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    status = models.BooleanField(default=False)

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_user_id(self):
        return self.user.id

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Patient(models.Model):
    """Модель пациента."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/patient_profiles/', null=True, blank=True)
    address = models.CharField(max_length=80)
    mobile = models.CharField(max_length=20, null=False)
    assigned_dentist = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    first_visit_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_user_id(self):
        return self.user.id

    def __str__(self):
        return f"{self.user.first_name}"


class ServiceCategory(models.Model):
    """Категория услуги (например: Диагностика, Лечение, Хирургия)"""
    name = models.CharField("Название категории", max_length=100)
    description = models.TextField("Описание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория услуги"
        verbose_name_plural = "Категории услуг"


class Service(models.Model):
    """Услуга клиники"""
    name = models.CharField("Название услуги", max_length=100)
    description = models.TextField("Описание", blank=True, null=True)
    duration = models.PositiveIntegerField("Длительность (мин)", default=60)
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(null=True)
    description = models.TextField('Жалобы', blank=True, null=True)
    status = models.BooleanField(default=True)
    is_attended = models.BooleanField('Пациент пришёл', null=True, blank=True, default=None)
    comment = models.TextField('Комментарий врача', blank=True, null=True)
    document = models.FileField('Документ', upload_to='doctor_notes/', null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"

class AppointmentDocument(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='appointment_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Файл для {self.appointment.id}"