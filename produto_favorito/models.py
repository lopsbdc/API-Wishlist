from django.db import models
from clientes.models import Clientes


# Create your models here.
class Produto(models.Model):
    email = models.ForeignKey("clientes.Clientes", on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)


    class Meta:
        unique_together = [['email', 'produto']]

    def __str__(self):
        return self.produto