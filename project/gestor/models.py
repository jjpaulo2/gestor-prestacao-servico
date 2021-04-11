from django.db import models


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=150, verbose_name="Nome completo")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    telefone = models.CharField(max_length=15, verbose_name="Telefone / Celular")
    email = models.EmailField(verbose_name="E-mail")

    class Meta:
        verbose_name_plural = "clientes"
        verbose_name = "cliente"
    

    def __str__(self):
        return f'Cliente #{self.id}: {self.nome}'
