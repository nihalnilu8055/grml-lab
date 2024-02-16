from django import forms
from . models import *

class Enquiry_form(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields='__all__'

class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class Appointment_form(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'