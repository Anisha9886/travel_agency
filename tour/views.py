from django.shortcuts import render,redirect
from .forms import *
from django import contrib
from django.contrib import messages
import requests
from .models import *


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created Succesfully for {username}!!!")
            return redirect('login')
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request,'register.html',context)

def addreview(request):
    return render(request,'addreview.html')

def dashboard(request):
    data = Popularplace.objects.all()
    data1 = Popularplace1.objects.all()
    return render(request,'dashboard.html',{'d': data,'e':data1})

def booktour(request,pk=None):
    place = Popularplace.objects.get(id=pk)
    form = BookTourForm()
    context = {
        'form': form,
        'place': place
    }
    return render(request,'booktour.html',context)

def booktourone(request,pk=None):
    place1 = Popularplace1.objects.get(id=pk)
    form = BookTourForm()
    context = {
        'form': form,
        'place1': place1
    }
    return render(request,'booktourone.html',context)


def application(request):
    if request.method == 'POST':
        form = BookTourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

