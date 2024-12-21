from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Manages, WorksIn, Patient, Doctor, AppointmentMakes

# Create your views here.
def index(request):
    return render(request, 'reception/home.html')

def new_patient(request):
    success = None
    if request.method == 'POST':
        patient_tc = request.POST.get('patient_tc')
        patient_name = request.POST.get('patient_name')
        patient_surname = request.POST.get('patient_surname')
        patient_phone = request.POST.get('patient_phone')
        patient_address = request.POST.get('patient_address')
        patient_birthdate = request.POST.get('patient_birthdate')
        gender = request.POST.get('gender')

        new_patient = Patient(
            patient_tc=patient_tc,
            patient_name=patient_name,
            patient_surname=patient_surname,
            patient_phone=patient_phone,
            patient_address=patient_address,
            patient_birthdate=patient_birthdate,
            gender=gender
        )
        new_patient.save()
        success = True
    return render(request, 'reception/new_patient.html', {"success":success})

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
