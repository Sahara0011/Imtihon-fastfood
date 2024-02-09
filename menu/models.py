from django.db import models


# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='product/')
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BookTable(models.Model):
    name = models.CharField(max_length=100)





