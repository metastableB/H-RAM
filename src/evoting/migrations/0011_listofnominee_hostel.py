# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0010_auto_20150317_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofnominee',
            name='hostel',
            field=models.CharField(max_length=30, default=0),
            preserve_default=False,
        ),
    ]
