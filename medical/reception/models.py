from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_tc = models.IntegerField()
    emp_name = models.CharField(max_length=50)
    emp_surname = models.CharField(max_length=50)
    emp_phone = models.CharField(max_length=15)
    profession = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.emp_name} {self.emp_surname}"
    
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.dept_name}"
    
class Manages(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    since = models.DateField()

    def __str__(self):
        return f"{self.emp_id} manages {self.dept_id}"
    
class WorksIn(models.Model):
    dept_id = models.ForeignKey(Department, on_delete=models.PROTECT)
    emp_id = models.ForeignKey(Employee, on_delete=models.PROTECT)
    since = models.DateField()
    till = models.DateField()
    
    def __str__(self):
        return f"{self.emp_id} works in {self.dept_id}"
    
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_tc = models.IntegerField(unique=True)
    patient_name = models.CharField(max_length=50)
    patient_surname = models.CharField(max_length=50)
    patient_phone = models.CharField(max_length=20)
    patient_address = models.CharField(max_length=225)
    patient_birthdate = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.patient_name} {self.patient_surname} {self.patient_id}"
    
class Doctor(models.Model):
    doc_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    doc_name = models.CharField(max_length=50)
    doc_title = models.CharField(max_length=255)
    room_no = models.IntegerField(unique=True)
    work_start = models.TimeField()
    word_end = models.TimeField()

class AppointmentMakes(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.patient_id} makes an appointment with {self.doc_id}"
    
    
