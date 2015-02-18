# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignStory',
            fields=[
                ('design_story_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('description', models.TextField()),
                ('cover_photo', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('portfolio', models.ForeignKey(to='Portfolios.Portfolio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entry_id', models.AutoField(serialize=False, primary_key=True)),
                ('context', models.TextField(blank=True)),
                ('date', models.DateField(blank=True)),
                ('bucket_link', models.CharField(max_length=255)),
                ('design_story', models.ForeignKey(to='Portfolios.DesignStory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='subdomain',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
