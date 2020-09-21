"""HomeCookups URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MerchantManagement import views as merchant_views
from CustomerManagement import views as customer_views
from FoodManagement import views as food_views
from OrderManagement import views as order_views
from BillManagement import views as bill_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Merchant/', merchant_views.showMerchants, name='Merchant'),
    path('Customer/',customer_views.showCustomers, name = 'Customer' ),
    path('Food/', food_views.showFoods, name='Food'),
    path('Order/', order_views.showOrders, name='Order'),
    path('Bill/', bill_views.showBills, name='Bill')
]
