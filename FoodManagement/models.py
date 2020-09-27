from django.db import models
from MerchantManagement.models import Merchant

# Create your models here.
class Food(models.Model):
    Food_Name = models.CharField(max_length=200)
    Food_Desc = models.FileField(upload_to='files/constitution/')
    Food_Img = models.ImageField(upload_to='images/logo/',default=1)
    Food_Price = models.FloatField(max_length=200)

    merchant = models.ForeignKey(Merchant,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.Food_Name