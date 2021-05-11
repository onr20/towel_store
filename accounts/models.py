from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='images/')


    ROLES_CHOICES = (
        ("ADM", "Admin"),
        ("USR", "User")
    )
    role = models.CharField(
        max_length=3,
        choices=ROLES_CHOICES,
        default="USR",
    )

    COMM_CHOICES = (
        ("PST", "Post Mail"),
        ("EML", "E-Mail"),
    )

    preferred_communication_channel = models.CharField(
        max_length=3,
        choices=COMM_CHOICES,
        default="EML",
    )




    def __str__(self):
        if self.user.first_name:
            return self.user.first_name
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} {self.surname}"