from django.contrib import admin
from .models import *


class HospitalAdmin(admin.ModelAdmin):
    list_display =['hospital_id','hospital_name','hospital_phonenumber']
admin.site.register(Hospital,HospitalAdmin)


class DonarAdmin(admin.ModelAdmin):
    list_display=['id','name','city','contact_number']

admin.site.register(Donor,DonarAdmin)
# Register your models here.
# organdonation
#organdonation23
