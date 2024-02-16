from django.contrib import admin
from . models import *

# Register your models here.
class Enquiry_display(admin.ModelAdmin):
    list_display=['name','email','phone','messge']
admin.site.register(Enquiry,Enquiry_display)

class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','subject','messge']
admin.site.register(Contact,Contact_display)

class Appointment_display(admin.ModelAdmin):
    list_display=['name','email','phone','date','time','gender','age','address','messge']
admin.site.register(Appointment,Appointment_display)