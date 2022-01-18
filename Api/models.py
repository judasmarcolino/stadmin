from django.db import models
from django.db.models.fields import AutoField

# Create your models here.


class Trabalhador (models.Model):
    id = AutoField(primary_key=True)
    nome = models.CharField( max_length=50)
    profissao = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    nuit = models.CharField(max_length=50)
    ContaBancaria =models.CharField(max_length=50)
    tipoDeContrado = models.CharField

    



class Fornecedor (models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)


