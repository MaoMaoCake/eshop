from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,help_text='Name of the product')
    picture = models.ImageField()
    price = models.DecimalField(decimal_places=2,max_digits=10,help_text='eg. 19.99')
    description = models.TextField(help_text="Products Description")
    new = models.BooleanField(default=True)
    best_seller = models.BooleanField(default=False)
    def __str__(self):
        return self.product_name