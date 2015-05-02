# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0011_auto_20150423_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designstory',
            name='description',
            field=models.TextField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
