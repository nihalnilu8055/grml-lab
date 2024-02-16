from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . models import *
from . forms import *
from django.contrib import messages
# Create your views here.

def index(requst):
    contxt={}
    form=Enquiry_form()
    if requst.method == 'POST':
        if 'save' in requst.POST:
            form=Enquiry_form(requst.POST)
            form.save()
            messages.success(requst,'SEND SUCCESSFULLY')
    enquiry=Enquiry.objects.all()
    contxt['enquiry']=enquiry
    contxt['form']=form
    return render(requst,'index.html',contxt)

def about(requst):
    return render(requst,'about.html')

def package(requst):
    return render(requst,'packages.html')

def blog(requst):
    return render(requst,'blog.html')

def branches(requst):
    return render(requst,'branches.html')

def gallery(requst):
    return render(requst,'gallery.html')

def executive_package(requst):
    return render(requst,'executive-package.html')

def ayush_gold(requst):
    return render(requst,'ayush-gold')

def ayush_silver(requst):
    return render(requst,'ayush-silver.html')

def ayush_general(requst):
    return render(requst,'ayush-general.html')

def cardiac(requst):
    return render(requst,'cardiac.html')

def lab_chambakkara(requst):
    return render(requst,'gmrl-chambakkara')

def lab_kolenchery(requst):
    return render(requst,'lab-kolenchery')

def lab_thrippunithura(requst):
    return render(requst,'lab-thrippunithura.html')

def lab_vadakkekotta(requst):
    return render(requst,'lab-vadakkekotta.html')

def molecular(requst):
    return render(requst,'molecular.html')

def radiology(requst):
    return render(requst,'radiologyy.html')

def test(requst):
    return render(requst,'test.html')

def contact(requst):
    contxt={}
    form=Contact_form()
    if requst.method == 'POST':
        if 'save' in requst.POST:
            form=Contact_form(requst.POST)
            form.save()
            messages.success(requst,'error')
    contact=Contact.objects.all()
    contxt['contact']=contact
    contxt['form']=form
    return render(requst,'contact-us.html',contxt)

def appointment(requst):
    contxt={}
    form=Appointment_form()
    if requst.method == 'POST':
        if 'save' in requst.POST:
            form=Appointment_form(requst.POST)
            form.save()
            messages.success(requst,'UR APPOINTMENT BOOKING IS SUCCESSFULL')
    appointment=Appointment.objects.all()
    contxt['appointment']=appointment
    contxt['form']=form
    return render(requst,'appointment.html',contxt)

def dept(requst):
    return render(requst,'dept.html')

# def register(requst):
#     return render(requst,'register/index.html')