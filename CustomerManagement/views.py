from django.shortcuts import render
from .models import Customer



def showCustomers(request):
    customerList = Customer.objects.all()
    context = {
        'customer': customerList
    }

    print(customerList)

    return render(request, 'CustomerManagement/CustomerList.html', context)





