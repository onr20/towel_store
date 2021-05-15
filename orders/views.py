from django.shortcuts import render
from .models import Order
from accounts.models import Account


def view_basket(request):
    user = request.user
    basket = []
    if user.is_authenticated:
        account = Account.objects.get(user=user)
        basket = Order.objects.get(client=account, active=True).order_lines.all()
        print("Hello, the user is here")

    
    return render(request, "orders/active_basket.html", context={"basket": basket})


def add_to_basket(request, order_line_id):
    pass


def remove_from_basket(request, order_line_id):
    pass


