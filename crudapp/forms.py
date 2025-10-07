from django import forms
from django.forms import ModelForm
from crudapp.models import register
from crudapp.models import profile
from crudapp.models import book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Reg(forms.ModelForm):
    class Meta:
        model=register
        fields=['name','mobile','age','gender','branch']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-controler','placeholder':'enter your name'}),
            'mobile':forms.TextInput(attrs={'class':'form-controler','placeholder':'enter your mobile number'}),
            'age':forms.NumberInput(attrs={'class':'form-controler','placeholder':'enter your age'}),
            'gender':forms.RadioSelect(attrs={'type':'radio','placeholder':'select your gender'}),
            'branch':forms.Select(attrs={'class':'form-controler'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields="__all__"


class Book(forms.ModelForm):
    class Meta:
        model=book
        fields=['name','mobile','service','email','date','time']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-controler','placeholder':'enter your name'}),
            'mobile':forms.TextInput(attrs={'class':'form-controler','placeholder':'enter your mobile number'}),
            'service':forms.RadioSelect(attrs={'type':'checkbox','placeholder':'select services'}),
            'email':forms.EmailInput(attrs={'type':'email','placeholder':'enter mail'}),
            'date':forms.DateInput(attrs={'type':'date','class': 'form-control','placeholder':'enter date'}),
            'time':forms.TimeInput(attrs={'type':'time','class': 'form-control','placeholder':'enter time'})
        }

class registrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-controler'}),
            'last_name':forms.TextInput(attrs={'class':'form-controler'}),
            'username':forms.TextInput(attrs={'class':'form-controler'}),
            'email':forms.EmailInput(attrs={'class':'form-controler'})
        }