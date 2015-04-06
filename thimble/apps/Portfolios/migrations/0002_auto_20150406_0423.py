# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_auto_20150405_0639'),
        ('Portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('commenter', models.ForeignKey(to='Users.Designer')),
                ('design_story', models.ForeignKey(to='Portfolios.DesignStory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design_story', models.ForeignKey(to='Portfolios.DesignStory')),
                ('liker', models.ForeignKey(to='Users.Designer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('liker', 'design_story')]),
        ),
        migrations.AddField(
            model_name='designstory',
            name='comments',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designstory',
            name='likes',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designstory',
            name='wip',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
