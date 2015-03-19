# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0003_auto_20150311_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofnominee',
            old_name='postition',
            new_name='position',
        ),
    ]
