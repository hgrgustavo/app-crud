# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'clientes'


class Pedidos(models.Model):
    clientes = models.ForeignKey(Clientes, models.DO_NOTHING)
    produtos = models.ForeignKey('Produtos', models.DO_NOTHING)
    data_pedido = models.DateField()

    class Meta:
        managed = False
        db_table = 'pedidos'
        unique_together = (('id', 'clientes', 'produtos'),)


class Produtos(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'produtos'
