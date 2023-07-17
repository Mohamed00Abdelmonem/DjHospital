from django.db import models

# Create your models here.

class Patient(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=3,choices=[('F',"Female"),('M',"Male")],default='M')
    Address = models.TextField()
    ContactNumber = models.CharField(max_length=20)
    Email = models.EmailField()

    def __str__(self) -> str:
        return self.FirstName




class Department(models.Model):
    DepartmentName = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.DepartmentName    

class Doctor(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=3,choices=[('F',"Female"),('M',"Male")],default='M')
    Specialty = models.CharField( max_length=100,
        choices=[
            ('cardiology', 'Cardiology'),
            ('neurology', 'Neurology'),
            ('pediatrics', 'Pediatrics'),
            ('orthopedics', 'Orthopedics'),
            ('gynecology', 'Gynecology'),
            ('oncology', 'Oncology'),
            ('dermatology', 'Dermatology'),
        ])
    ContactNumber = models.CharField(max_length=20)
    Email = models.EmailField()
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)



    def __str__(self) -> str:
        return self.FirstName
    


class Appointment(models.Model):
    PatientID = models.ForeignKey(Patient, on_delete=models.SET_NULL, null= True)
    DoctorID  = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null= True)
    AppointmentDate = models.DateField()
    StartTime = models.TimeField()
    EndTime  = models.TimeField()

    def __str__(self) -> str:
        return self.AppointmentDate.strftime("%Y-%m-%d")

