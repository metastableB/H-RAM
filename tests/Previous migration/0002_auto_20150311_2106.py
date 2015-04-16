# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomNumber', models.CharField(max_length=5)),
                ('floor', models.CharField(max_length=5)),
                ('count', models.IntegerField(default=0, max_length=4)),
                ('x', models.IntegerField(max_length=3)),
                ('y', models.IntegerField(max_length=3)),
                ('uId', models.ForeignKey(to='sessionapp.UserList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='roompreference',
            name='valid',
            field=models.IntegerField(default=1, max_length=1),
            preserve_default=True,
        ),
    ]
