# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0015_listofhostel'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofnominee',
            name='nomineesRollNo',
            field=models.CharField(max_length=10, default=0),
            preserve_default=False,
        ),
    ]
