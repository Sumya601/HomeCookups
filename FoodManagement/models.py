from django.db import models
from MerchantManagement.models import Merchant
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    RATING_OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(max_length=10, choices = RATING_OPTIONS, default='4')
    comment = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.rating

class Food(models.Model):
    Food_Name = models.CharField(max_length=200)
    Food_Desc = models.FileField(upload_to='files/constitution/')
    Food_Price = models.FloatField(max_length=200)
    Food_Category = models.CharField(max_length=50)

    Food_Image = models.ImageField(upload_to='Foods/images/',blank=True, default="images/default.jpg")

    merchant = models.ForeignKey(Merchant,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.Food_Name