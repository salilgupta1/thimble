# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0003_collection_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='details',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='min_quantity',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='product_number',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='retail_price',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='wholesale_price',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
