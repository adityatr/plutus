# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('money', '0002_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='MintTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=30)),
                ('original_description', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('acc_type', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('acc_name', models.CharField(max_length=30)),
                ('fk_to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]