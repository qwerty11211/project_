from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

from .models import User, Medications
from doctor.models import Doctor


def user_exist(credential):
    username = credential.cleaned_data.get("username")
    password = credential.cleaned_data.get("password")
    user = User.objects.filter(username=username, password=password)
    if user:
        return True
    else:
        return False


def valid_username(credential):
    username = credential.cleaned_data.get("username")
    user = User.objects.filter(username=username)
    if user:
        return False
    else:
        return True


def login_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if user_exist(form):
                messages.add_message(request, messages.INFO, 'Logged in!')
                return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


def register_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and valid_username(form):
            form.save()
            return redirect('/user/login')
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def landingpage(request):
    return render(request, 'user/landingpage.html')


def list_doctors(request):
    data = Doctor.objects.filter()
    context = {
        'doctor_info': data,
    }
    return render(request, 'user/list_doctor.html', context)


def dashboard(request):

    medications = Medications.objects.filter()
    context = {
        'medications': medications,

    }
    return render(request, 'user/dashboard.html', context)
