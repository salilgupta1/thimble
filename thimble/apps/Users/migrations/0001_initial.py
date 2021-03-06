# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.CharField(default=b'', max_length=255, blank=True)),
                ('bio', models.TextField(max_length=250, blank=True)),
                ('location', models.CharField(max_length=100, blank=True)),
                ('following', models.BigIntegerField(default=0, blank=True)),
                ('followers', models.BigIntegerField(default=0, blank=True)),
                ('boutique_name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field=b'username')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.CharField(default=b'', max_length=255, blank=True)),
                ('bio', models.TextField(max_length=250, blank=True)),
                ('location', models.CharField(max_length=100, blank=True)),
                ('following', models.BigIntegerField(default=0, blank=True)),
                ('followers', models.BigIntegerField(default=0, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field=b'username')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followee', models.ForeignKey(related_name='follow_followee', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(related_name='follow_follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('follower', 'followee')]),
        ),
    ]
