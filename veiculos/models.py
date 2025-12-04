from django.db import models
from estacionamento.models import Estacionamento

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    km = models.FloatField(default=0)
    status = models.CharField(max_length=20, default='disponivel')
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.modelo} ({self.placa})"
