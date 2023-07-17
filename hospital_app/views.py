from django.shortcuts import render, redirect
from .models import Doctor,Patient, Appointment
from .forms import DoctorForm
# Create your views here.

def index(reuest):
    return render(reuest,'index.html')

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


def appointment(request):
    data = Appointment.objects.all()
    return render(request, 'appointment.html', {'context':data})


def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DoctorForm()
        return render(request, 'creat_doctor.html', {'form': form})    
    
def edit_doctor(request, id_doctor):
        pass

def delete_doctor(request, id_doctor):
        pass