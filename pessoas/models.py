from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    dt_nascimento = models.DateField('Data de Nascimento')
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['nome']

class Cuidador(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=12, blank=True)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Cuidador"
        verbose_name_plural = "Cuidadores"
        ordering = ['nome']

