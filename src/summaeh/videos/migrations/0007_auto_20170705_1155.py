# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-05 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20170705_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='event',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='events.Event'),
        ),
    ]
