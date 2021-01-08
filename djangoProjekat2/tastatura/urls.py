from django.urls import path

from . import views

app_name = 'tastatura'

urlpatterns = [
    path('', views.dash, name='home'),
    path('proizvodjac', views.createProizvodjac , name= 'proizvodjac'),
    path('tastatura' , views.createTastatura , name = 'tastatura')


]