from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    landmark = models.CharField(max_length=50)


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    landmark = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comments(models.Model):
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment