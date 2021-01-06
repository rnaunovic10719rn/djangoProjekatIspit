from django.contrib import admin

# Register your models here.

from .models import Tastatura,Proizvodjac

admin.site.register(Tastatura)
admin.site.register(Proizvodjac)