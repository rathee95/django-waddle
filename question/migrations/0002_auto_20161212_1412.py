# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-12 08:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='upvoted_by',
            field=models.ManyToManyField(blank='true', related_name='questions_upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]