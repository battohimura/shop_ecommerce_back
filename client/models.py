from django.db import models

class Client(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name='nombre'
    )
    address = models.CharField(
        max_length=200,
        verbose_name='dirección'
    )
    email = models.EmailField(
        verbose_name='correo electrónico'
    )
    phone = models.CharField(
        max_length=80,
        verbose_name='teléfono'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
