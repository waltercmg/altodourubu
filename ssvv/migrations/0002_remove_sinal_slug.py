# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-03 02:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssvv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sinal',
            name='slug',
        ),
    ]
