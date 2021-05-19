from django.urls import path
from . import views


app_name = "orders"
urlpatterns = [
    path("view/", views.view_basket, name="basket_view"),
    path("add/<product_id>/", views.add_to_basket, name="basket_add"),
    path("remove/<order_line_id>/", views.remove_from_basket, name="basket_remove"),
    path("empty_basket/<order_id>/", views.empty_basket, name="empty_basket"),
    path("checkout/<order_id>/", views.checkout, name="checkout"),
]