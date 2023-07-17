from django.contrib import admin
from .models import Patient, Doctor, Department , Appointment
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Appointment)