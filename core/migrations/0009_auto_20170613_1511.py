# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170612_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caderno',
            name='lista',
        ),
        migrations.AddField(
            model_name='listacaderno',
            name='cadernos',
            field=models.ManyToManyField(to='core.Caderno'),
        ),
    ]
