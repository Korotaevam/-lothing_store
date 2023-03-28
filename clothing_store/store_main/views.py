from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'store_main/index.html')


def products(request):
    return render(request, 'store_main/products.html')
