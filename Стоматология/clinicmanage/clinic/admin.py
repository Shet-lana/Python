from django.contrib import admin
from .models import Doctor, Patient, Appointment, Service, ServiceCategory, AppointmentDocument

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(ServiceCategory)

@admin.register(AppointmentDocument)
class AppointmentDocumentAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'file', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['appointment__patient__user__first_name', 'appointment__patient__user__last_name']