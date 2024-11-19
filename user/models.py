from django.db import models
from restaurant.models import Company
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="users", null=True, blank=True)

    def __str__(self):
        return self.username
