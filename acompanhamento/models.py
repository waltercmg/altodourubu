# encoding=utf8  
# coding=UTF-8

from __future__ import unicode_literals

from django.db import models
from pessoas.models import Cuidador, Paciente
from ssvv.models import Sinal
from django.utils import timezone

# Create your models here.
class Afericao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Aferição"
        verbose_name_plural = "Aferições"
        ordering = ['dt_criacao']

class Dado(models.Model):
    afericao = models.ForeignKey(Afericao, on_delete=models.CASCADE)
    sinal = models.ForeignKey(Sinal, on_delete=models.CASCADE)
    valor = models.CharField('Valor', max_length=7)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    
    def __str__(self):
        return str(self.afericao.id)
    
    class Meta:
        verbose_name = "Dado"
        verbose_name_plural = "Dados"
        ordering = ['sinal']

