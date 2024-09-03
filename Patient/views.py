from django.shortcuts import render,redirect,reverse
from .models import Patient_model 
from Donor.models import Donor_model
from .utils import is_compatible

# Create your views here.

def request_blood(request):
    return render(request,'patient/request_blood.html')

def match_donors(blood_group):
    all_donors = Donor_model.objects.all()
    compatible_donors = [donor for donor in all_donors if is_compatible(donor.blood_group, blood_group)]
    return compatible_donors

def save_to_db(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        blood_group = request.POST.get('bloodgroup')
        blood_units = request.POST.get('amount')
        phone_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        reason = request.POST.get('reason')
        
        Patient_model.objects.create(
            full_name=full_name,
            blood_group=blood_group,
            blood_units=blood_units,
            phone_number=phone_number,
            email=email,
            address=address,
            reason=reason,
        )
        
        matching_donors = match_donors(blood_group)
        content = {
        'name':full_name,
        'blood':blood_group,
        'matching_donors': matching_donors,
        }
        
        return render(request,'Patient/saved.html',content)
    return redirect('Patient:request_blood')

def saved(request):
    return render(request,"patient/saved.html")