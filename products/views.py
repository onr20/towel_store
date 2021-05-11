from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    return render(request,'index.html')


def products(request):
    my_products = Product.objects.all()
    return render(request, "products/products_list.html", context={"products": my_products})


