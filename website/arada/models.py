from django.db import models

# Create your models here.
# shopinfo
# product

class ShopInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
     return self.name

   

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    price = models.FloatField(null=True)

    def __str__(self) -> str:
     return self.product_name

