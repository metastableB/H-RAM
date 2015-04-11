# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0008_auto_20150319_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roompreference',
            name='preferedRoom',
            field=models.CharField(max_length=4),
            preserve_default=True,
        ),
    ]
