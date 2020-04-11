from django.db import models


class Product_types(models.Model):
    name = models.CharField(max_length=254, default='')

    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'

    def __str__(self):
        return self.name.replace('_', ' ')


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_count = models.DecimalField(
        max_digits=3, decimal_places=0, default=0)
    image = models.ImageField(upload_to='images')
    product_type = models.ForeignKey(
        Product_types, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name.replace('_', ' ')
