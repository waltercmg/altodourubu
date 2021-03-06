# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-03 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0003_auto_20190403_0303'),
        ('ssvv', '0003_auto_20190403_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afericao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('cuidador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.Cuidador')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.Paciente')),
            ],
            options={
                'ordering': ['dt_criacao'],
                'verbose_name': 'Aferi\xe7\xe3o',
                'verbose_name_plural': 'Aferi\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Dado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=7, verbose_name='Valor')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('afericao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acompanhamento.Afericao')),
                ('sinal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssvv.Sinal')),
            ],
            options={
                'ordering': ['sinal'],
                'verbose_name': 'Dado',
                'verbose_name_plural': 'Dados',
            },
        ),
    ]
