# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20161116_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='sub_header',
            field=models.TextField(default=''),
        ),
    ]