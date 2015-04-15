# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0003_auto_20150311_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomlist',
            name='rollNumber',
            field=models.CharField(default=datetime.datetime(2015, 3, 11, 23, 11, 40, 918991, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
