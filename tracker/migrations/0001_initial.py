# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('company_link', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField()),
                ('shift_length', models.IntegerField(default=8)),
                ('status', models.CharField(choices=[('R', 'Regular'), ('PT', 'Part Time'), ('P', 'Probationary'), ('I', 'Intern'), ('T', 'Terminated'), ('A', 'Admin')], max_length=2)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('EL', 'Emergency Leave'), ('SL', 'Sick Leave'), ('VL', 'Vacation Leave')], max_length=2)),
                ('reason', models.TextField()),
                ('date_filed', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_filed_for', models.DateTimeField()),
                ('date_reviewed', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(choices=[('A', 'Approved'), ('R', 'Rejected'), ('P', 'Pending')], max_length=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves', to='tracker.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.CharField(max_length=140)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='tracker.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('message', models.TextField()),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Offset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_ended', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('date_applied', models.DateTimeField()),
                ('status', models.CharField(choices=[('A', 'Approved'), ('R', 'Rejected'), ('P', 'Pending')], max_length=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offsets', to='tracker.Employee')),
            ],
        ),
    ]
