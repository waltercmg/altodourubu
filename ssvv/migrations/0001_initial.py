# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-02 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
        ),
    ]
