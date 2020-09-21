from django.shortcuts import render
from .models import Order


# Create your views here.
def showOrders(request):
    orderList = Order.objects.all()
    context = {
        'Order': orderList
    }
    return render(request, 'OrderManagement/OrderList.html', context)
