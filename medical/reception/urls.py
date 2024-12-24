from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('enroll_patient/', views.new_patient, name='new_patient'),
    path("patients/", views.existing_patient, name="existing_patient"),
    path("emergency/", views.emergency, name="emergency"),
    path("visitors/", views.visitors, name="visitors"),
    path("appointments_and_reservations/", views.appointments_and_reservations, name="appointments_and_reservations"),
]
