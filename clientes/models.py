from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    foto_faceid = models.ImageField(upload_to='faces/', null=True, blank=True)
    senha_temporaria = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.nome
