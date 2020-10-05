from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from .models import Food
# from .models import Review
from .forms import FoodForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def showFoods(request):
    foodList = Food.objects.all()

    if request.method == 'POST':
        foodList  = Food.objects.filter(Food_Name__icontains = request.POST['search'])
        #Food_Desc = Food.objects.filter(description__icontains = request.POST['search'])
        Food_Category = Food.objects.filter(Food_Category__icontains=request.POST['search'])

        #foodList = Food_Name | Food_Category | Food_Desc # C = A U B set operation

        foodList = foodList | Food_Category

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
            return redirect('insertFood')
            message = "Food is inserted to DB. You can insert a new food now"
            form = FoodForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'FoodManagement/insertFood.html', context)


def main_home(request):
    return render(request, 'main_home.html')

def showDetails(request, Food_id):
    searched_food = get_object_or_404(Food, id=Food_id)
    context = {
        'search': searched_food
    }
    return render(request, 'FoodManagement/detail_product_view.html', context)

    # searched_food = get_object_or_404(Food, id=Food_id)
    #
    # form = ReviewForm()
    #
    # if request.method == "POST":
    #     form = ReviewForm(request.POST)
    #
    #     if form.is_valid:
    #         instance = form.save(commit=False)
    #         instance.user = request.user
    #         instance.save()
    #
    #         searched_food.reviews.add(instance)
    #         searched_food.save()
    #
    # context = {
    #     'search': searched_food,
    #     'form': form
    # }
    # return render(request, 'FoodManagement/detail_product_view.html', context)

@login_required
def review_after_complete(request, food_id):

    already_reviewed = False

    searched_product = get_object_or_404(Food, id=food_id)

    user_list = searched_product.reviews.filter(user=request.user)
    print(user_list, len(user_list))
    if len(user_list) != 0:
        already_reviewed = True


    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_product.reviews.add(instance)
            searched_product.save()

            #return redirect('my-orders')

    context = {
        'search': searched_product,
        'form': form,
        'already_reviewed': already_reviewed
    }
    return render(request, 'FoodManagement/detail_product_view_review.html', context)