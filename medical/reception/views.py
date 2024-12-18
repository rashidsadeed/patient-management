from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Manages, WorksIn, Patient, Doctor, AppointmentMakes

# Create your views here.
def index(request):
    return render(request, 'reception/home.html')

def new_patient(request, data):
    return render(request, 'reception/new_patient.html')

def existing_patient(request):
    patient_id = request.GET.get('id')
    surname = request.GET.get('surname')
    this_patient = None
    error_message = None
    
    try:
        if patient_id:
            this_patient = Patient.objects.get(patient_id=patient_id)
        elif surname:
            this_patient = Patient.objects.get(patient_surname=surname)
        elif patient_id and surname:
            this_patient = Patient.objects.get(patient_id=patient_id, patient_surname=surname)
            
    except Patient.DoesNotExist:
        error_message = "Patient not found."

    return render(request, 'reception/existing_patient.html', {'patient': this_patient, "error_message": error_message})

def emergency(request):
    return render(request, 'reception/emergency.html')

def visitors(request):
    return render(request, 'reception/visitor_management.html')

def appointments_and_reservations(request):
    return render(request, 'reception/doctor_room_availavility.html')
