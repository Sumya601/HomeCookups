from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    Phone_Number = models.IntegerField(unique=True)
    Address = models.CharField(max_length=200)


    def __str__(self):
        return self.customer_name
