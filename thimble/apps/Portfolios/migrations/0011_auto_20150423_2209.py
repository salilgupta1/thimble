# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0010_auto_20150423_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_desc',
            field=models.TextField(default=b'', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_title',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
