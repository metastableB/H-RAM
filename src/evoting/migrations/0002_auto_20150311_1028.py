# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '__first__'),
        ('evoting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ballot',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('position', models.CharField(max_length=50)),
                ('nomineeSelected', models.CharField(max_length=60)),
                ('goodPasswordUsed', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VotersList',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('goodPassword', models.CharField(max_length=64)),
                ('evilPassword', models.CharField(max_length=64)),
                ('voterDetails', models.ForeignKey(to='sessionapp.UserList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ballot',
            name='voter',
            field=models.ForeignKey(to='evoting.VotersList'),
            preserve_default=True,
        ),
    ]
