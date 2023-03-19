from django.urls import path
from .views import login_page, register_page, landingpage,  list_doctors, dashboard

urlpatterns = [

    path('', landingpage, name='landingpage'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('list/', list_doctors, name='list_doctors'),

    path('dashboard/', dashboard, name='dashboard'),





]
