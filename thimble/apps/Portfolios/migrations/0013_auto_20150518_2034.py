# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_auto_20150423_2215'),
        ('Portfolios', '0012_auto_20150424_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('likes', models.BigIntegerField(default=0, blank=True)),
                ('comments', models.BigIntegerField(default=0, blank=True)),
                ('wip', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=255, blank=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('designer', models.ForeignKey(to='Users.Designer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('designer', 'title')]),
        ),
    ]
