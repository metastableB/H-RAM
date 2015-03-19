# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatesList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidatesName', models.CharField(max_length=60)),
                ('position', models.CharField(max_length=50)),
                ('eligibility', models.IntegerField(max_length=1)),
                ('supporters', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListOfNominee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomineesName', models.CharField(max_length=60)),
                ('postition', models.CharField(max_length=50)),
                ('NumberOfVotes', models.IntegerField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
