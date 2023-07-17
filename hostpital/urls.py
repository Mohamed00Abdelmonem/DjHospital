"""
URL configuration for hostpital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from hospital_app.views import list_doctors, detail_doctor,list_patients, detail_patient, appointment,index, create_doctor,edit_doctor,delete_doctor,create_patient,edit_patinet,delete_patient,create_appointments,edit_appointments,delete_appointments
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('doctors/', list_doctors),
    path('doctors/<int:id_doctor>', detail_doctor),
    path('patients/', list_patients),
    path('patients/<int:id_patient>', detail_patient),
    path('appointment/',appointment),
    # crud operation to Doctor
    path('doctors/create_doctor/',create_doctor),
    path('doctors/<int:id_doctor>/edit_doctor/', edit_doctor),
    path('doctors/<int:id_doctor>/delete_doctor/', delete_doctor),
    # crud operation to Patient
    path('patients/create_patient/',create_patient),
    path('patients/<int:id_patient>/edit_patient/', edit_patinet),
    path('patients/<int:id_patient>/delete_patient/', delete_patient),
    # crud operation to Appointment
    path('appointment/create_appointment/',create_appointments),
    path('appointment/<int:id_appointment>/edit_appointment/', edit_appointments),
    path('appointment/<int:id_appointment>/delete_appointment/', delete_appointments),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
