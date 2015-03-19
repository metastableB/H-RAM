# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0004_auto_20150311_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateslist',
            name='firstSupportersSupport',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidateslist',
            name='secondSupportersSupport',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
    ]
