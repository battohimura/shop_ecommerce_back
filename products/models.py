from django.db import models

class Product(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name='nombre'
    )
    image = models.ImageField(
        verbose_name='imagen'
    )
    details = models.CharField(
        max_length=600,
        verbose_name='detalle'
    )
    price = models.CharField(
        max_length=80,
        verbose_name='precio'
    )
    gender = models.CharField(
        max_length=80,
        verbose_name='género'
    )
    stock = models.PositiveIntegerField(
        verbose_name='stock'
    )
    deleted = models.BooleanField(
        default=False,
        verbose_name='eliminado'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'