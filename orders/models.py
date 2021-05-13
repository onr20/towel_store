from django.db import models
from products.models import Product
from accounts.models import Account


class Order(models.Model):
    client = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="orders")
    date_of_submission = models.DateField()

    STATUS_CHOICES = (
        ("NP", "Not Paid"),
        ("PD", "Paid"),
        ("SH", "Shipped"),
        ("DL", "Delivered")
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default="PD"
    )


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    number_of_products = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")