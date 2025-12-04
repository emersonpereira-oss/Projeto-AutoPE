from django.db import models

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=30)
    status = models.CharField(max_length=20, default='pendente')

    def __str__(self):
        return f"Pagamento {self.id} - R${self.valor}"
