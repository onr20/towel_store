from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def products(request):
    return render(request, "products/products_list.html")


