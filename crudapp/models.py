from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)

    rollno=models.CharField(max_length=30)

    age=models.IntegerField()

    mobile=models.CharField(max_length=10)

    email=models.EmailField(max_length=30)
    
    adress=models.CharField(max_length=30)

    def _str_(self):
       return self.name+" "+self.email

class register(models.Model):
    genders=[('female','female'),('male','male')]
    branches=[('select','select'),('cse','cse'),('ece','ece'),('mech','mech'),('eee','eee'),('it','it')]
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=genders,null=True)
    branch=models.CharField(max_length=10,choices=branches,null=True)

class profile(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="profiles/")

class book(models.Model):
    service=[('Haircut & styling','Haircut & styling'),('facials & skincare','facials & skincare'),('Bridal makeup','Bridal makeup')]
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    service=models.CharField(max_length=50,choices=service,null=True)
    email=models.EmailField(max_length=50,null=True)
    date=models.DateField()
    time=models.TimeField()
    
