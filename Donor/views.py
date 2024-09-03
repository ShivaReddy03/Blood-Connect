from django.shortcuts import render,redirect
from .models import Donor_model

# Create your views here.
def donate_req(request):
    return render(request,'Donor/donate_blood.html')

def save_to_db(request):
    if request.method=="POST":
        
        # Extract form data from request.POST
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        blood_group = request.POST.get('blood_group')
        blood_units = request.POST.get('unit')
        phone_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        medical_history = request.POST.get('medical_history')

        # Create and save a new Donor instance
        Donor_model.objects.create(
            full_name=full_name,
            age=age,
            blood_group=blood_group,
            blood_units=blood_units,
            phone_number=phone_number,
            email=email,
            medical_history=medical_history,
        )
        return redirect("Donor:saved")
    return redirect("Donor:donate_req")

def saved(request):
    return render(request,"Donor/saved.html")