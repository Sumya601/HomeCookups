from django.shortcuts import render
from .models import Food


# Create your views here.
def showFoods(request):
    foodList = Food.objects.all()
    context = {
        'Food': foodList
    }
    return render(request, 'FoodManagement/FoodList.html', context)
