from django.db import models

# Create your models here.
class Merchant(models.Model):
    Merchant_Name = models.CharField(max_length=100)
    Food_Name = models.CharField(max_length=200)
    Business_Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200, unique=True)
    NID = models.CharField(max_length=200, unique=True)
    Phone_Number = models.IntegerField(max_length=200, unique=True)
    Address = models.CharField(max_length=200)


