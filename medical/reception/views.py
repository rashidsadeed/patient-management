from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Department, Manages, WorksIn, Patient, Doctor, AppointmentMakes, Receptionist, Visitor
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        password = request.POST.get('password')

        try:
            receptionist = Receptionist.objects.get(emp_id=emp_id, password=password)
            if receptionist is not None:
                request.session['emp_id'] = receptionist.emp_id.emp_id
                request.session['emp_name'] = f"{receptionist.emp_id.emp_name} {receptionist.emp_id.emp_surname}"
                return redirect('index')
            else:
                return HttpResponse(f"You are not authorized to access this page.")
        except Receptionist.DoesNotExist:
            return HttpResponse("Invalid credentials. Please try again.")
    return render(request, 'reception/login.html')


def index(request):
    emp_id = request.session.get('emp_id')
    emp_name = request.session.get('emp_name')
    context = {
        'emp_id': emp_id,
        'emp_name': emp_name
    }
    return render(request, 'reception/home.html', context)

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
    patient_id = request.GET.get('search_id')
    name = request.GET.get('search_name')
    surname = request.GET.get('search_surname')
    this_patient = None
    error_message = None
    
    try:
        if patient_id and surname:
            this_patient = Patient.objects.get(patient_id=patient_id, patient_surname=surname)
        elif patient_id:
            this_patient = Patient.objects.get(patient_id=patient_id)
        elif surname:
            this_patient = Patient.objects.get(patient_surname=surname)
        else:
            this_patient = Patient.objects.get(patient_name=name)
        
            
    except Patient.DoesNotExist:
        error_message = "Patient not found."

    return render(request, 'reception/existing_patient.html', {'patient': this_patient, "error_message": error_message})

def emergency(request):
    if request.method == "POST":
        admission_datetime = request.POST['admission_datetime']
        patient_name = request.POST['patient_name']
        patient_condition = request.POST['patient_condition']

        return HttpResponse("Emergency patient has been admitted successfully!")

    return render(request, 'reception/emergency.html')


def visitors(request):
    success = None
    if request.method == "POST":
        visitor_patient_id = request.POST['visitor_patient_id']
        visitor_tc = request.POST['visitor_tc']
        visitor_name = request.POST['visitor_name']
        visitor_surname = request.POST['visitor_surname']
        visitor_closeness = request.POST['visitor_closeness']
        visitor_roomnumber = request.POST['visitor_roomnumber']
        visitor_entry = request.POST['visitor_entry']
        visitor_exit = request.POST['visitor_exit']

        # Assuming you have a Visitor model and you want to save the data
        try:
            patient = Patient.objects.get(patient_id=visitor_patient_id)
            visitor = Visitor(
                patient=patient,
                visitor_tc=visitor_tc,
                visitor_name=visitor_name,
                visitor_surname=visitor_surname,
                patient_closeness=visitor_closeness,
                patient_room=visitor_roomnumber,
                visitor_entry_time=visitor_entry,
                visitor_exit_time=visitor_exit
            )
            visitor.save()
            success = True
            return HttpResponse("Visitor information saved successfully.")
        except Patient.DoesNotExist:
            return HttpResponse("Patient not found.")

    return render(request, 'reception/visitor_management.html', {"success": success})

def appointments_and_reservations(request):
    doc_surname = request.GET.get('doc_name')
    patient_tc = request.GET.get('patient_tc')
    matching_appointments = None
    context = {}

    if doc_surname and patient_tc:
        try:
            doctor = Doctor.objects.get(doc_id__emp_surname=doc_surname)
            patient = Patient.objects.get(patient_tc=patient_tc)
            matching_appointments = AppointmentMakes.objects.filter(doc_id=doctor, patient_id=patient.patient_id)
        except Doctor.DoesNotExist or Patient.DoesNotExist or AppointmentMakes.DoesNotExist:
            return HttpResponse("entry not found.")
        
        context = {
            'appointments': matching_appointments,
            'doctor': doctor,
            'patient': patient
        }
    return render(request, 'reception/doctor_room_availavility.html', context)
