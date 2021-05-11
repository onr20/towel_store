from django.urls import path
from . import views

app_name= 'products'
urlpatterns = [
    path('', views.index, name="index"),
    path("products/", views.ProductsViewList.as_view(), name="products_list"),
    path("products/<pk>/", views.ProductDetailView.as_view(), name="product_view")

]
