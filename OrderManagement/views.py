from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def showOrders(request):
    orderList = Order.objects.all()
    context = {
        'Order': orderList
    }
    return render(request, 'OrderManagement/OrderList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'OrderManagement/registration.html', context)

@login_required
def insertOrder(request):
    message = ""
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Order is inserted to DB. You can insert a new order now"
            form = OrderForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'OrderManagement/insertOrder.html', context)
