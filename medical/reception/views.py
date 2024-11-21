from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'reception/home.html')

def new_patient(request):
    return render(request, 'reception/new_patient.html')

def existing_patient(request):
    return render(request, 'reception/existing_patient.html')

def emergency(request):
    return render(request, 'reception/emergency.html')

def visitors(request):
    return render(request, 'reception/visitor_management.html')

def appointments_and_reservations(request):
    return render(request, 'reception/doctor_room_availavility.html')
