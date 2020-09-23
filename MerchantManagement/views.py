from django.shortcuts import render
from .models import Merchant
from .forms import MerchantForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def showMerchants(request):
    merchantList = Merchant.objects.all()
    context = {
        'Merchant': merchantList
    }
    return render(request, 'MerchantManagement/MerchantList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form
    }
    return render(request, 'MerchantManagement/registration.html', context)

@login_required
def insertMerchant(request):
    message = ""
    form = MerchantForm()

    if request.method == "POST":
        form = MerchantForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Merchant is inserted to DB. You can insert a new merchant now"
            form = MerchantForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'MerchantManagement/insertMerchant.html', context)