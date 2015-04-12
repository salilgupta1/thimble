# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0003_auto_20150408_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designstory',
            name='wip',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together=set([('title', 'design_story')]),
        ),
    ]
