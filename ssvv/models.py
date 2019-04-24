# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sinal(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=10)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Sinal"
        verbose_name_plural = "Sinais"
        ordering = ['nome']
    
#class Paciente(models.Model):
    #nome = models.CharField('Nome', max_length=100)

#class Cuidador(models.Model):
    #nome = models.CharField('Nome', max_length=100)
    
#class Afericao(models.Model):
    #numero = 
    #data = models.DateField('Data da Afericao', auto_now_add=True)