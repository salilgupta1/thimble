# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('collection', models.ForeignKey(to='Portfolios.Collection')),
                ('commenter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entry_id', models.AutoField(serialize=False, primary_key=True)),
                ('entry_title', models.CharField(max_length=60)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('bucket_link', models.CharField(default=b'', max_length=255, blank=True)),
                ('cover_photo', models.CharField(default=b'', max_length=255, blank=True)),
                ('entry_desc', models.TextField(default=b'', max_length=200, blank=True)),
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
                ('liker', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
            unique_together=set([('liker', 'collection')]),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('designer', 'title')]),
        ),
    ]
