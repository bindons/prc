# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name=b'verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name=b'Unique Verification UUID'),
        ),
    ]
