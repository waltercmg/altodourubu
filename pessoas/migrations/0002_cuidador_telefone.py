# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-03 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuidador',
            name='telefone',
            field=models.CharField(blank=True, max_length=12, verbose_name='Telefone'),
        ),
    ]