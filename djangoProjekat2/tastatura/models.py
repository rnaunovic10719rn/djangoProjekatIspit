from django.db import models


# Create your models here.


class Proizvodjac(models.Model):
    naziv = models.CharField(max_length=50)

    def __str__(self):
        return self.naziv


class Tastatura(models.Model):
    naziv = models.CharField(max_length=100)
    cena_DIN = models.IntegerField(default=0)
    proizvedeno_Od = models.ForeignKey(Proizvodjac, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv
