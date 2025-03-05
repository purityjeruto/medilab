from django.shortcuts import render, redirect,get_object_or_404
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
       return redirect('/show')

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

def show (request):
    all=appointment.objects.all()
    return render(request, 'show.html',{'all':all})

def delete(request,id):
    deleteappointment=appointment.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/show')

def edit(request,id):
    appointment1= get_object_or_404(appointment,id=id)
    if request.method =='POST':
            appointment1.name = request.POST['name'],
            appointment1.email = request.POST['email'],
            appointment1.phone= request.POST['phone'],
            appointment1.date= request.POST['date'],
            appointment1.department= request.POST['department'],
            appointment1.doctor= request.POST['doctor'],
            appointment1.message = request.POST['message']
            appointment1.save()
            return redirect('/show')
    else:
        return render(request, 'edit.html', {'appointment1': appointment1})



