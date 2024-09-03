from django.db import models

# Create your models here.
class Donor_model(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    blood_units = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    medical_history = models.TextField(null=True ,blank=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table= "Donor_details_table"