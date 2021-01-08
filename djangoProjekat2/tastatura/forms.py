from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class TastaturaForm(ModelForm):
    class Meta:
        model = Tastatura
        fields = '__all__'

class ProizvodjacForm(ModelForm):
    class Meta:
        model = Proizvodjac
        fields = '__all__'