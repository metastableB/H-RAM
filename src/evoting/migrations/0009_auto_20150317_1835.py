# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0008_auto_20150317_1832'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListOfSecretries',
            new_name='ListOfSecretry',
        ),
        migrations.RenameField(
            model_name='listofsecretry',
            old_name='nameOfSecretory',
            new_name='nameOfSecretry',
        ),
        migrations.RenameField(
            model_name='listofsecretry',
            old_name='roolNoOfSecretory',
            new_name='roolNoOfSecretry',
        ),
    ]
