# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20150220_0131'),
        ('Portfolios', '0002_auto_20150218_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='designstory',
            name='designer',
            field=models.ForeignKey(default='', to='Users.Designer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='designstory',
            name='name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='subdomain',
            field=models.SlugField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='designstory',
            unique_together=set([('designer', 'name')]),
        ),
        migrations.RemoveField(
            model_name='designstory',
            name='portfolio',
        ),
    ]
