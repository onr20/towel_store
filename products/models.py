from django.db import models
from accounts.models import Author


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="images/")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    
    PRODUCT_TYPE_CHOICES = (
        ("CTN", "Cotton"),
        ("LNN", "Linen")
    )
    product_type = models.CharField(
        max_length=3,
        choices=PRODUCT_TYPE_CHOICES,
        default="CTN"
    )
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
