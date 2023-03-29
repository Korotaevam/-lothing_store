from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):


    context = {
        "title": "Store"
    }
    return render(request, 'store_main/index.html', context)


def products(request):
    products_all = Product.objects.all()
    categosies_all = ProductCategory.objects.all()
    context = {
        "title": "Каталог",
        'products': products_all,
        'categories': categosies_all
    }
    return render(request, 'store_main/products.html', context)

