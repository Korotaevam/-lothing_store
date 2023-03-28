from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        "title": "Store"
    }
    return render(request, 'store_main/index.html', context)


def products(request):
    context = {
        "title": "Каталог"
    }
    return render(request, 'store_main/products.html', context)
