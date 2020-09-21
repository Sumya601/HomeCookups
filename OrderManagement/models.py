from django.db import models
from FoodManagement.models import Food
from MerchantManagement.models import Merchant
from CustomerManagement.models import Customer


# Create your models here.
class Order(models.Model):
    Order_Type = models.CharField(max_length=100)
    Order_Status = models.CharField(max_length=200)

    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.Order_Type
