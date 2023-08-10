from django.db import models

from client.models import Client
from products.models import Product

class Sale(models.Model):
    product = models.ManyToManyField(
        Product
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.DO_NOTHING
    )
    quantity = models.PositiveIntegerField(
        verbose_name='cantidad'
    )
    total = models.PositiveIntegerField(
        verbose_name='total'
    )

    def __str__(self):
        return self.id
