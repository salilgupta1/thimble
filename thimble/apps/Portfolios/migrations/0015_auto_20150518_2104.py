# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0014_auto_20150518_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('piece_id', models.AutoField(serialize=False, primary_key=True)),
                ('piece_title', models.CharField(default=b'', max_length=60, blank=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('front_view', models.CharField(default=b'', max_length=255, blank=True)),
                ('back_view', models.CharField(default=b'', max_length=255, blank=True)),
                ('collection', models.ForeignKey(to='Portfolios.Collection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='piece',
            unique_together=set([('piece_title', 'collection')]),
        ),
    ]
