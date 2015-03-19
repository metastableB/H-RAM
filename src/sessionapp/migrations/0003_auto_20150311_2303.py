# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0002_auto_20150311_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomlist',
            name='uId',
        ),
        migrations.AlterField(
            model_name='friendspreference',
            name='preferedfriendUId1',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friendspreference',
            name='preferedfriendUId2',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friendspreference',
            name='preferedfriendUId3',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friendspreference',
            name='preferedfriendUId4',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friendspreference',
            name='preferedfriendUId5',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
