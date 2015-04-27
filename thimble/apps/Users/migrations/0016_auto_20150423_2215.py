# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0015_auto_20150423_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='bio',
            field=models.TextField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='designer',
            name='location',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
