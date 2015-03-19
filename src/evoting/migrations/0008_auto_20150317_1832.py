# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0007_auto_20150317_1757'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListOfSecretories',
            new_name='ListOfSecretries',
        ),
    ]
