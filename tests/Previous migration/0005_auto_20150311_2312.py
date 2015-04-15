# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0004_roomlist_rollnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomlist',
            name='rollNumber',
            field=models.CharField(default=b'0', max_length=10),
            preserve_default=True,
        ),
    ]
