from django.db import models
from clientes.models import Cliente

class TentativaAcesso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    sucesso = models.BooleanField()
    motivo = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Tentativa {self.id} - Cliente {self.cliente.id}"
