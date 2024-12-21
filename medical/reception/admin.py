from django.contrib import admin
from .models import Employee, Department, Manages, WorksIn, Patient, Doctor, AppointmentMakes, Visitor, PatientOf
# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Manages)
admin.site.register(WorksIn)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(AppointmentMakes)
admin.site.register(Visitor)
admin.site.register(PatientOf)
