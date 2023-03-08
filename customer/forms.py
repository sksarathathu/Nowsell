from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from customer.models import Userprofile,Products

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=["pic","bio"]


class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=["owner","name","description","condition","category","location","price","status","image"]


