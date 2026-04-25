from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# <input type="text" name="username" placeholder="write your name">
class RegistrationFrom(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'write your name..',
        'class': 'form-control'
        }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'write your email..',
        'class': 'form-control'
        }))
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'write your name..',
        'class': 'form-control'
        }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'write your surname..',
        'class': 'form-control'
        }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'write your password..',
        'class': 'form-control'
        }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat your password..',
        'class': 'form-control'
        }))
    
    class Meta:
        model=User
        #set the order of displaying the fields in the form
        #ustanavlayem poryadok otobrajeniya poley na stranitse 
        fields=["first_name","username", "email", "last_name", "password1", "password2"] 


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'write your name..',
        'class': 'form-control'
        }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'write your password..',
        'class': 'form-control'
        }))

    class Meta:
        model=User
        fields=["username", "password"]

    