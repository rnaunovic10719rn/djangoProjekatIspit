from django.shortcuts import render , redirect
from .models import *
from .forms import *
# Create your views here.

def userPage(request):
    proizvodjac = Proizvodjac.objects.all()
    tastatura = Tastatura.objects.all()
    return render(request, 'tastatura/user.html', {'proizvodjac': proizvodjac, 'tastatura': tastatura})


def dash(request):
    proizvodjac = Proizvodjac.objects.all()
    tastatura = Tastatura.objects.all()
    return render(request, 'tastatura/dashboard.html', {'proizvodjac': proizvodjac, 'tastatura': tastatura})

def createProizvodjac(request):
    form = ProizvodjacForm()
    if request.method == 'POST':
        form = ProizvodjacForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form': form}

    return render(request, 'tastatura/proizvodjac.html', context)

def createTastatura(request):
    form = TastaturaForm()
    if request.method == 'POST':
        form = TastaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form': form}

    return render(request, 'tastatura/tastatura.html', context)