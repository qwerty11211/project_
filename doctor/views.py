from django.shortcuts import render
from .models import Doctor
from user.models import Appointments
import datetime


def dashboard(request, doctor_id):
    doctor_details = Doctor.objects.get(id=doctor_id)
    appointments = Appointments.objects.filter().order_by('datetime')
    context = {
        'appointments': appointments,
        'doctor': doctor_details,
        'todays_date': datetime.datetime.now().date().strftime('%d-%m-%Y'),

    }
    return render(request, 'doctor/dashboard.html', context)


def doctor_details(request, doctor_id):
    doctor_details = Doctor.objects.get(id=doctor_id)
    context = {
        'doctor': doctor_details,
    }

    return render(request, 'user/doctor-details.html', context)


def book_appointment(request, doctor_id):
    doctor_details = Doctor.objects.get(id=doctor_id)
    return render(request, 'user/book_appointment.html', {
        'doctor': doctor_details,
    })


def checkout(request, doctor_id):
    doctor_details = Doctor.objects.get(id=doctor_id)
    return render(request, 'user/checkout.html', {
        'doctor': doctor_details,
    })


def book_success(request, doctor_id):
    doctor_details = Doctor.objects.get(id=doctor_id)
    return render(request, 'user/booking_sucess.html', {
        'doctor': doctor_details,
    })


def videocall(request, doctor_id):
    doctor_details = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctor/video_call.html', {
        'doctor': doctor_details,
    })


def add_prescription(request, doctor_id):
    doctor_details = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctor/add_prescription.html', {
        'doctor': doctor_details,
    })
