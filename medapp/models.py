from django.db import models

# Create your models here.
class patient(models.Model):
    fullname=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.fullname

class doctor(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=100)
    email=models.EmailField()
    status=models.CharField(max_length=100)
    age=models.IntegerField()
    qualification=models.CharField(max_length=50)

    def __str__(self):
        return self.name
#create staff model
#fname,lname,position,4num,email,date hired,
class staff(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    email=models.EmailField()
    datehired=models.DateField()

    def __str__(self):
        return self.firstname



#return fname&lname
#create a ward model
#name,total beds,unoccupiedbeds
#return tha name
class ward(models.Model):
    wardname=models.CharField(max_length=50)
    totalbeds=models.IntegerField()
    unoccupiedbeds=models.IntegerField()

    def __str__(self):
        return self.wardname

class appointment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    date=models.DateField()
    department=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject= models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name