from django.urls import path
from . import views


app_name = "orders"
urlpatterns = [
    path("view/", views.view_basket, name="basket_view"),
    path("add/<product_id>/", views.add_to_basket, name="basket_add"),
    path("remove/<product_id>/", views.remove_from_basket, name="basket_remove1"),
]