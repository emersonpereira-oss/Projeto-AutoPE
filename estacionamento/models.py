from django.db import models

class Estacionamento(models.Model):
    via = models.CharField(max_length=10)
    fila = models.CharField(max_length=10)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"Via {self.via} - Fila {self.fila}"
