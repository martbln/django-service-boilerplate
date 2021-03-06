# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-28 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cors',
            options={'verbose_name': 'Кросс-доменное разрешение', 'verbose_name_plural': 'Кросс-доменные разрешения'},
        ),
        migrations.AlterModelOptions(
            name='historicalcors',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Кросс-доменное разрешение'},
        ),
        migrations.AlterField(
            model_name='cors',
            name='cors',
            field=models.CharField(max_length=255, help_text='Название домена допущенного делать междоменные запросы, например: staff-front.pik-software.ru или localhost:3000', unique=True),
        ),
        migrations.AlterField(
            model_name='historicalcors',
            name='cors',
            field=models.CharField(db_index=True, help_text='Название домена допущенного делать междоменные запросы, например: staff-front.pik-software.ru или localhost:3000', max_length=255),
        ),
    ]
