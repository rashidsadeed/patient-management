from django.contrib import admin
from .models import Employee, Department, Manages, WorksIn, Patient, Doctor, AppointmentMakes, Visitor, PatientOf, Receptionist
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_tc', 'emp_name', 'emp_surname', 'emp_phone', 'profession')

class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'password')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Receptionist, ReceptionistAdmin)
admin.site.register(Department)
admin.site.register(Manages)
admin.site.register(WorksIn)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(AppointmentMakes)
admin.site.register(Visitor)
admin.site.register(PatientOf)
