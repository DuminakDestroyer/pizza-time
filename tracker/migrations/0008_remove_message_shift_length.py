# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_message_shift_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='shift_length',
        ),
    ]