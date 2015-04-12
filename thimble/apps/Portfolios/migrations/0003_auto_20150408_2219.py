# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0002_auto_20150406_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='designstory',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='context',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='date',
        ),
        migrations.AddField(
            model_name='designstory',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='date_created',
            field=models.DateField(default=None, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='designstory',
            unique_together=set([('designer', 'title')]),
        ),
    ]
