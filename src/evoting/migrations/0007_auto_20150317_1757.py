# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0006_candidateslist_candidatesrollno'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfSecretories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('hostelsName', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('roolNoOfSecretory', models.CharField(max_length=10)),
                ('nameOfSecretory', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostsForElection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('hostelsName', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='listofnominee',
            name='NumberOfVotes',
            field=models.IntegerField(max_length=7, default=0),
            preserve_default=True,
        ),
    ]
