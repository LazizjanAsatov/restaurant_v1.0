from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
