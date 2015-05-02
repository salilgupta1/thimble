# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0009_entry_entry_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designstory',
            name='description',
            field=models.TextField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='designstory',
            name='title',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
    ]
