from django.urls import path
from .views import dashboard, add_prescription, videocall, book_success, doctor_details, checkout, book_appointment


urlpatterns = [

    path('<doctor_id>/', doctor_details, name='doctor-details'),
    path('<doctor_id>/book', book_appointment, name='book_appointment'),
    path('<doctor_id>/success', book_success, name='book_success'),
    path('<doctor_id>/dashboard', dashboard, name='dashboard'),
    path('<doctor_id>/call', videocall, name='videocall'),
    path('<doctor_id>/add_prescription',
         add_prescription, name='add_prescription'),


]
