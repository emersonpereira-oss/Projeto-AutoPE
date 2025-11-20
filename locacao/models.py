from django.db import models
from clientes.models import Cliente
from veiculos.models import Veiculo
from pagamentos.models import Pagamento

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pagamento = models.OneToOneField(Pagamento, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_prevista = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)
    metodo_verificacao = models.CharField(max_length=20)

    def __str__(self):
        return f"Locação {self.id}"
