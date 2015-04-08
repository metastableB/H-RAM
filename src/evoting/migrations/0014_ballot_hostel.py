# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0013_supportersdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballot',
            name='hostel',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
