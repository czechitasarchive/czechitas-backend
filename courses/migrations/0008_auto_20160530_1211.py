# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20160530_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='couch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Couch'),
        ),
    ]
