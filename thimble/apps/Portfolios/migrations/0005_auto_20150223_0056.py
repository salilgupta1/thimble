# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20150221_2050'),
        ('Portfolios', '0004_auto_20150220_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='designstory',
            name='subdomain',
            field=models.ForeignKey(to='Users.Designer', default='test', to_field=b'subdomain'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='designstory',
            unique_together=set([('subdomain', 'name')]),
        ),
        migrations.RemoveField(
            model_name='designstory',
            name='designer',
        ),
    ]
