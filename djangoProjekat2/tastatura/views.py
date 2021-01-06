from django.shortcuts import render
from .models import *
# Create your views here.

def userPage(request):
    proizvodjac = Proizvodjac.objects.all()
    tastatura = Tastatura.objects.all()
    return render(request, 'tastatura/user.html', {'proizvodjac': proizvodjac, 'tastatura': tastatura})