# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_auto_20150423_2215'),
        ('Portfolios', '0013_auto_20150518_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('collection', models.ForeignKey(to='Portfolios.Collection')),
                ('commenter', models.ForeignKey(to='Users.Designer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', models.ForeignKey(to='Portfolios.Collection')),
                ('liker', models.ForeignKey(to='Users.Designer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('liker', 'collection')]),
        ),
    ]
