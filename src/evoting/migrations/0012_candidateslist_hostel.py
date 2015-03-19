# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0011_listofnominee_hostel'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateslist',
            name='hostel',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
