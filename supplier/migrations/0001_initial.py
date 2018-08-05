# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 08:18
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=30)),
                ('supplier_contact', models.IntegerField()),
                ('supplier_address', models.CharField(max_length=30)),
                ('supplier_description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]