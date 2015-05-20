# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('Users', '0016_auto_20150423_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to_field=b'username', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.CharField(default=b'', max_length=255, blank=True)),
                ('bio', models.TextField(max_length=250, blank=True)),
                ('location', models.CharField(max_length=100, blank=True)),
                ('following', models.BigIntegerField(default=0, blank=True)),
                ('followers', models.BigIntegerField(default=0, blank=True)),
                ('boutique_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
