from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from .models import Order, OrderLine
from products.models import Product
from accounts.models import Account
from .forms import CartAddProductForm
import datetime


def view_basket(request):
    user = request.user
    basket = []
    if user.is_authenticated:
        account = Account.objects.get(user=user)
        if Order.objects.filter(client=account, active=True).exists():
            active_order = Order.objects.get(client=account, active=True)
        else:
            active_order = Order.objects.create(
                client=account,
                active=True
            )

        basket = active_order.order_lines.all()
        total_price = 0
        for item in basket:
            total_price += item.price * item.number_of_products
        



    
    return render(request, "orders/active_basket.html", context={"basket": basket, "active_order": active_order, "total_price": total_price})



@login_required
def add_to_basket(request, product_id):
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data["quantity"]
    else:
        return redirect(reverse("products:product_view", args=[product_id]))
    
    user = request.user
    account = Account.objects.get(user=user)

    if Order.objects.filter(client=account, active=True).exists():
        active_order = Order.objects.get(client=account, active=True)
    else:
        active_order = Order.objects.create(
            client=account,
            active=True
        )

    product = Product.objects.get(id=product_id)
    if active_order.order_lines.filter(product=product).exists():
        order_line = active_order.order_lines.get(product=product)
        order_line.number_of_products += quantity
        order_line.save()
    else:
        OrderLine.objects.create(
            product=product,
            order=active_order,
            number_of_products=quantity,
            price=product.price
        )
    return redirect("orders:basket_view")



def remove_from_basket(request, order_line_id):
    order_line = OrderLine.objects.get(id=order_line_id)
    order_line.delete()
    return redirect("orders:basket_view")


def empty_basket(request, order_id):
    active_order = Order.objects.get(id=order_id)
    OrderLine.objects.filter(order=active_order).delete()

    return redirect("orders:basket_view")


def checkout(request, order_id):
    paid_order = Order.objects.get(id=order_id)
    paid_order.active = False
    paid_order.status = "PD"
    paid_order.date_of_submission = datetime.date.today()
    paid_order.save()

    paid_basket = paid_order.order_lines.all()
    total_price = 0
    for item in paid_basket:
        total_price += item.price * item.number_of_products

    return render(request, "orders/checkout_page.html", context={"paid_basket": paid_basket, "total_price": total_price})
