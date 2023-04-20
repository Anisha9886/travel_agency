from django import forms
from django.forms import widgets 
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserCretionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class DateInput(forms.DateInput):
    input_type = 'date'


class BookTourForm(forms.ModelForm):
    class Meta:
       model = Booking
       widgets = {'date': DateInput()} 
       fields = ['firstname','lastname','email','address','place','date','totaladults']
