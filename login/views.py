from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'login/dashboard.html')  # Ensure this template exists

def register(request):
    return render(request, 'login/register.html')

def save_data(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:
            # Create a new user
            try:
                User.objects.create_user(username=username, password=password, email=email)
                messages.success(request, 'User registered successfully')
                return redirect('login')  # Redirect to the login page after registration
            except ValueError as e:
                messages.error(request, str(e))
                return render(request, 'login/register.html')

    # For GET requests or if POST data is invalid
    return render(request, 'login/register.html')

def login(request):
    return render(request, 'login/login.html')

def after_login(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('pass_word')

        # Authenticate the user
        temp = authenticate(request, username=username, password=password)
        
        if temp is not None:
            # Log the user in
            dj_login(request, temp)  # Correct usage: `login(request, user)`
            messages.success(request, "Login successful!")
            return redirect(reverse('home'))  # Redirect to a success page or home
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login/login.html")
        
    return render(request,"login/login.html")

@login_required(login_url="/login/")
def home(request):
    return  render(request,"login/home.html")