from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="clients"
    )

    def __str__(self):
        return self.name
