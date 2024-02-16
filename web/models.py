from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    messge=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    messge=models.TextField(max_length=255)

class Appointment(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    gender=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.TextField()
    messge=models.TextField()