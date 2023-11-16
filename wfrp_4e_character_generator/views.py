from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms.signup import RegistrationForm

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # redirect to main page
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})
