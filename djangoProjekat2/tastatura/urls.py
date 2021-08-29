from django.urls import path

from . import views

app_name = 'tastatura'

urlpatterns = [
    path('', views.dash, name='home'),
    path('proizvodjac', views.proizvodjac, name='proizvodjac'),
    path('tastatura', views.tastatura, name='tastatura'),
    path('user', views.user, name='user'),
]