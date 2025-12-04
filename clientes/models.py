from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    foto_faceid = models.ImageField(upload_to='faces/', null=True, blank=True)

    # senha armazenada como hash
    senha = models.CharField(max_length=128, null=True, blank=True)


    def set_password(self, raw_password):
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)

    def __str__(self):
        return self.nome
