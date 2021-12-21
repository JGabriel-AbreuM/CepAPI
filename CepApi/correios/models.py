from django.db import models
from django.db.models.fields import CharField
from .validate import validaCPF

class Endereco(models.Model):
    bairro = CharField(max_length=100)
    cep = CharField(validators=[validaCPF], max_length=9)
    cidade = CharField(max_length=100)
    logradouro = CharField(max_length=100)
    uf  = CharField(max_length=2)

    def __str__(self):
        return f'{self.cidade} - {self.uf}'