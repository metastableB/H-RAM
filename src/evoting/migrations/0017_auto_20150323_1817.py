# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0016_listofnominee_nomineesrollno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofsecretary',
            old_name='roolNoOfSecretary',
            new_name='rollNoOfSecretary',
        ),
    ]
