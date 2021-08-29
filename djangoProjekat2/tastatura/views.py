from django.shortcuts import render, redirect
from .models import *
from .forms import *


def dash(request):
    proizvodjac = Proizvodjac.objects.all()
    tastatura = Tastatura.objects.all()
    total_proizvodjac = proizvodjac.count()
    total_tastatura = tastatura.count()
    return render(request, 'tastatura/dashboard.html', {'proizvodjac': proizvodjac, 'tastatura': tastatura, 'total_proizvodjac': total_proizvodjac, 'total_tastatura' : total_tastatura})

def proizvodjac(request):
    proizvodjac = Proizvodjac.objects.all()
    total_proizvodjac = proizvodjac.count()
    return render(request, 'tastatura/proizvodjac.html', {'proizvodjac': proizvodjac, 'total_proizvodjac': total_proizvodjac})

def tastatura(request):
    tastatura = Tastatura.objects.all()
    total_tastatura = tastatura.count()
    return render(request, 'tastatura/tastatura.html', {'tastatura': tastatura, 'total_tastatura': total_tastatura})