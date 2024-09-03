from django.contrib import admin
from .models import Patient_model

# Register your models here.

@admin.register(Patient_model)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'blood_group','blood_units', 'phone_number', 'email')
    search_fields = ('full_name', 'phone_number')
    list_filter = ('blood_group',)