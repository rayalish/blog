from django import forms
from .models import *

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'author': forms.HiddenInput(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }   