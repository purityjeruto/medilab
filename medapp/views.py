from django.shortcuts import render, redirect
from medapp.models import *
# Create your views here.
def home (request):
    return render(request,'index.html')
def about (request):
    return render(request,'about.html')
def starter(request):
    return render(request,'starter-page.html')
def services(request):
    return render(request,'services.html')
def departments(request):
    return render(request,'departments.html')
def doctors(request):
    return render(request,'doctors.html')
def appointment1(request):
    if request.method =='POST':
       myappointments = appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone= request.POST['phone'],
            date = request.POST['date'],
            department= request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
       myappointments.save()
       return redirect('/appointment')

    else:
          return render(request,'appointment.html')

def contact1(request):
    if request.method =='POST':
       mycontacts = contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject= request.POST['subject'],
            message = request.POST['message'],
        )
       mycontacts.save()
       return redirect('/contact')

    else:
          return render(request,'contact.html')
