# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-07 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movietheatre', '0003_auto_20200206_1847'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set([('screen', 'row', 'seat_number')]),
        ),
    ]
