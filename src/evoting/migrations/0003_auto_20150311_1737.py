# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0002_auto_20150311_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateslist',
            name='supporters',
        ),
        migrations.AddField(
            model_name='candidateslist',
            name='firstSupporter',
            field=models.CharField(default=datetime.datetime(2015, 3, 11, 12, 7, 43, 284215, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidateslist',
            name='secondSupporter',
            field=models.CharField(default=datetime.datetime(2015, 3, 11, 12, 7, 55, 85795, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
    ]
