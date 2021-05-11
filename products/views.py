from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

def index(request):
    return render(request,'index.html')


# def products(request):
#     my_products = Product.objects.all()
#     return render(request, "products/products_list.html", context={"products": my_products})


class ProductsViewList(ListView):
    template_name = "products/products_list.html"
    model = Product


class ProductDetailView(DetailView):    
    template_name = "products/product_view.html"
    model = Product

