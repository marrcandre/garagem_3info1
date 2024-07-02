from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(null=True, blank=True, default=0, max_digits=10, decimal_places=2)
    acessorios = models.ManyToManyField(Acessorio)

    def __str__(self):
        return f"{self.modelo} {self.cor} {self.ano} ({self.id})"

    class Meta:
        verbose_name_plural = "Veículos"
        verbose_name = "Veículo"
