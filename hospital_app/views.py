from django.shortcuts import render
from .models import Doctor,Patient
# Create your views here.

def list_doctors(request):
    data = Doctor.objects.all()
    return render(request, 'list_doctors.html', {'context':data})


def detail_doctor(request, id_doctor):
    data = Doctor.objects.get(id = id_doctor)
    return render(request, 'detail_doctor.html', {'context':data})


def list_patients(request):
    data = Patient.objects.all()
    return render(request, 'list_patient.html', {'context':data})


def detail_patient(request, id_patient):
    data = Patient.objects.get(id = id_patient)
    return render(request, 'detail_patient.html', {'context':data})
