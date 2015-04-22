# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0008_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry_desc',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
