from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Hospital(models.Model):
    hospital_id = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=300)
    hospital_Address= models.CharField(max_length=500)
    hospital_phonenumber= models.CharField(max_length=10)

    def __str__(self):
        return self.hospital_name
    

class Donor(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.ImageField(max_length=100)
    blood_grp = models.CharField(max_length=5)
    organ_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)

    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='donors')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    