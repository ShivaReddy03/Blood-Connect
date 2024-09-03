from django.contrib import admin
from .models import Donor_model

# Register your models here.

@admin.register(Donor_model)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'blood_group', 'phone_number', 'email')
    search_fields = ('full_name', 'phone_number')
    list_filter = ('blood_group',)