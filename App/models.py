from django.db import models


class Hospital(models.Model):
    
    hospital_name = models.CharField(max_length=300)
    hospital_address = models.CharField(max_length=500)  
    hospital_phonenumber = models.CharField(max_length=10)

    def __str__(self):
        return self.hospital_name
    

class Donor(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)  
    age = models.IntegerField()
    blood_grp = models.CharField(max_length=5)
    organ_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
