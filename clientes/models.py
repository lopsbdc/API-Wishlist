from django.db import models

# Create your models here.
class Clientes(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.email