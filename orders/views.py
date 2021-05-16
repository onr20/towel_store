from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Order
from accounts.models import Account
from .forms import CartAddProductForm


def view_basket(request):
    user = request.user
    basket = []
    if user.is_authenticated:
        account = Account.objects.get(user=user)
        basket = Order.objects.get(client=account, active=True).order_lines.all()

    
    return render(request, "orders/active_basket.html", context={"basket": basket})



@login_required
def add_to_basket(request, product_id):
    form = CartAddProductForm(request.POST)
    print(form.cleaned_data)
    quantity = form.cleaned_data["quantity"]
    print(quantity)
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
    pass


