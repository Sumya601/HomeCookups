from django.shortcuts import render
from .models import Food
from .forms import FoodForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def showFoods(request):
    foodList = Food.objects.all()
    context = {
        'Food': foodList
    }
    return render(request, 'FoodManagement/FoodList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'FoodManagement/registration.html', context)

@login_required
def insertFood(request):
    message = ""
    form = FoodForm()

    if request.method == "POST":
        form = FoodForm(request.POST,request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Food is inserted to DB. You can insert a new food now"
            form = FoodForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'FoodManagement/insertFood.html', context)