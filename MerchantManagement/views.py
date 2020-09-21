from django.shortcuts import render
from .models import Merchant


# Create your views here.
def showMerchants(request):
    merchantList = Merchant.objects.all()
    context = {
        'merchants': merchantList
    }
    return render(request, 'MerchantManagement/MerchantList.html', context)
