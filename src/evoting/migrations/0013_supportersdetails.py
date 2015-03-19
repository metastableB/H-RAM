# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0012_candidateslist_hostel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportersDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('candidatesRollNo', models.CharField(max_length=10)),
                ('candidatesName', models.CharField(max_length=60)),
                ('firstSupporter', models.CharField(max_length=60)),
                ('secondSupporter', models.CharField(max_length=60)),
                ('firstSupporterHashKey', models.CharField(max_length=64)),
                ('secondSupporterHashKey', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
