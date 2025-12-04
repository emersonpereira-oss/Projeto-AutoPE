from django.db import models

class Estacionamento(models.Model):
    via = models.CharField(max_length=20)
    fila = models.CharField(max_length=20)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Via {self.via} - Fila {self.fila}"
