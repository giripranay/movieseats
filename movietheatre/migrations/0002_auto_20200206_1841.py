# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietheatre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.IntegerField(unique=True),
        ),
    ]
