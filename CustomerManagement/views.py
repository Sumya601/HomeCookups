from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def showCustomers(request):
    customerList = Customer.objects.all()
    context = {
        'Customer': customerList
    }

    print(customerList)

    return render(request, 'CustomerManagement/CustomerList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'CustomerManagement/registration.html', context)

@login_required
def insertCustomer(request):
    message = ""
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST,)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Customer is inserted to DB. You can insert a new customer now"
            form = CustomerForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'CustomerManagement/insertCustomer.html', context)



