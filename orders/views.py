from django.shortcuts import render


def view_basket(request):
    
    return render(request, "orders/active_basket.html")


def add_to_basket(request, order_line_id):
    pass


def remove_from_basket(request, order_line_id):
    pass
