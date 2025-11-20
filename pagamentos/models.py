from django.db import models

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    metodo = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Pagamento {self.id} - R${self.valor}"
