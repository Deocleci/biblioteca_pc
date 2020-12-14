from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm
from django.contrib.postgres.forms import RangeWidget # for DateRangeField
from .models import Livro



class LivroForm(forms.ModelForm):
    
    class Meta:
        model = Livro
        fields =  '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'required':''}),
            'autor' : forms.TextInput(attrs={'class': 'form-control', 'required':''}),
            'codigo' : forms.TextInput(attrs={'class': 'form-control', 'required':''}),
            'editora' : forms.TextInput(attrs={'class': 'form-control', 'required':''})

        }

