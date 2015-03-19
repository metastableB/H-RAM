# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0009_auto_20150317_1835'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListOfSecretry',
            new_name='ListOfSecretary',
        ),
        migrations.RenameField(
            model_name='listofsecretary',
            old_name='nameOfSecretry',
            new_name='nameOfSecretary',
        ),
        migrations.RenameField(
            model_name='listofsecretary',
            old_name='roolNoOfSecretry',
            new_name='roolNoOfSecretary',
        ),
    ]
