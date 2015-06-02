# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('likes', models.BigIntegerField(default=0, blank=True)),
                ('comments', models.BigIntegerField(default=0, blank=True)),
                ('wip', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=255, blank=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('designer', models.ForeignKey(to='Users.Designer', to_field=b'user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('collection', models.ForeignKey(to='Portfolios.Collection')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('collection', models.ForeignKey(to='Portfolios.Collection')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
            name='like',
            unique_together=set([('content_type', 'object_id', 'collection')]),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('designer', 'title')]),
        ),
    ]
