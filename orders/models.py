from django.db import models
from products.models import Product
from accounts.models import Account
import datetime


class Order(models.Model):
    client = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="orders")
    date_of_submission = models.DateField(default=datetime.date.today)
    active = models.BooleanField()  # If active=True, it means an active basket but order wasn't made yet
    sum = models.DecimalField(max_digits=7, decimal_places=2, default=0)  # price of the whole order

    STATUS_CHOICES = (
        ("NP", "Not Paid"),
        ("PD", "Paid"),
        ("SH", "Shipped"),
        ("DL", "Delivered")
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default="NP"
    )

    def __str__(self):
        return f"Order of {self.client}, date: {self.date_of_submission}"


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    number_of_products = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2) # price of one line of order
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")

    class Meta:
        unique_together = [
            ['product', 'order'],
        ]

    def __str__(self):
        return f"{self.order} - {self.product}"

