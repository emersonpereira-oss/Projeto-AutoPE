from django.db import models
from clientes.models import Cliente
from veiculos.models import Veiculo
from pagamentos.models import Pagamento

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='locacoes')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='locacoes')
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_prevista = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pagamento = models.OneToOneField('pagamentos.Pagamento', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Locacao {self.id} - {self.cliente.nome}"
