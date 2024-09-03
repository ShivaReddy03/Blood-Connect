from django.db import models

# Create your models here.
class Patient_model(models.Model):
    full_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=10)
    blood_units = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    reason = models.TextField()
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table= "Patient_details_table"