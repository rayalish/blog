from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


from .models import User

class UserSignUpForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')
        
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        } 


class UserSignInForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

