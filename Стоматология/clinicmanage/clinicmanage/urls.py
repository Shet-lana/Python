"""
URL configuration for clinicmanage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from clinic import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('patient-signup/', views.patient_signup_view, name='patient-signup'),
    path('patient-dashboard/', views.patient_dashboard_view, name='patient-dashboard'),
    path('patient-appointment/', views.patient_appointment_view, name='patient-appointment'),
    path('patient-book-appointment/', views.patient_book_appointment_view, name='patient-book-appointment'),
    path('patient-view-appointment/', views.patient_view_appointment_view, name='patient-view-appointment'),
    path('doctor-dashboard/', views.doctor_dashboard_view, name='doctor-dashboard'),
    path('service-list/', views.service_list_view, name='service-list'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('logout/', LogoutView.as_view(template_name='clinic/index.html'), name='logout'),
    path('patient-edit-profile/', views.patient_edit_profile_view, name='patient-edit-profile'),
    path('doctor-appointment-detail/<int:appointment_id>/', views.doctor_appointment_detail_view, name='doctor-appointment-detail'),
    path('patient-list/', views.patient_list_view, name='patient-list'),
    path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment_view, name='cancel-appointment'),
    path('patient-detail/<int:patient_id>/', views.patient_detail_view, name='patient-detail'),
    path('reschedule-appointment/<int:appointment_id>/', views.reschedule_appointment_view, name='reschedule-appointment'),
    path('doctor-reschedule-appointment/<int:appointment_id>/', views.doctor_reschedule_appointment_view, name='doctor-reschedule-appointment'),
    path('get-available-slots-json/', views.get_available_slots_json, name='get_available_slots_json'),
    path('doctors/', views.doctors_view, name='doctors'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)