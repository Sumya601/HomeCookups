from django.shortcuts import render
from .models import Bill


# Create your views here.
def showBills(request):
    billList = Bill.objects.all()
    context = {
        'bills': billList
    }
    return render(request, 'OrderManagement/OrderList.html', context)
