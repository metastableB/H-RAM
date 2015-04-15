# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0005_auto_20150311_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomlist',
            old_name='count',
            new_name='counter',
        ),
    ]
