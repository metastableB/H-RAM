# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0006_auto_20150312_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendspreference',
            name='rollNumber',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
