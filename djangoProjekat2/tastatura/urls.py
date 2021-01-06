from django.urls import path

from . import views

app_name = 'tastatura'

urlpatterns = [
    path('', views.userPage, name='home'),


]