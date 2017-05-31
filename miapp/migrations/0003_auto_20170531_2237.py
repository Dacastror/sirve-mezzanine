# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-31 22:37
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20170531_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='text',
        ),
        migrations.AlterField(
            model_name='author',
            name='dob',
            field=mezzanine.core.fields.RichTextField(),
        ),
    ]