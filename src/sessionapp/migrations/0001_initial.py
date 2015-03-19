# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FriendsPreference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('preferedfriendUId1', models.IntegerField(max_length=10)),
                ('preferedfriendUId2', models.IntegerField(max_length=10)),
                ('preferedfriendUId3', models.IntegerField(max_length=10)),
                ('preferedfriendUId4', models.IntegerField(max_length=10)),
                ('preferedfriendUId5', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomPreference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rollNumber', models.CharField(max_length=10)),
                ('preferenceNumber', models.IntegerField(max_length=3)),
                ('preferedRoom', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentBioDataTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rollNumber', models.CharField(max_length=10)),
                ('jeeRegistrationNo', models.CharField(max_length=10)),
                ('jeeAIR', models.IntegerField(max_length=7)),
                ('name', models.CharField(max_length=50)),
                ('hostelAlloted', models.CharField(max_length=50)),
                ('courseAdmitted', models.CharField(max_length=50)),
                ('dateOfBirth', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('bloodGroup', models.CharField(max_length=3)),
                ('height', models.IntegerField(max_length=3)),
                ('weight', models.IntegerField(max_length=3)),
                ('category', models.CharField(max_length=20)),
                ('cast', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=20)),
                ('fathersName', models.CharField(max_length=50)),
                ('guardiansName', models.CharField(max_length=50)),
                ('guardiansProfession', models.CharField(max_length=50)),
                ('parentsOrGuardiansAnnualIncom', models.IntegerField(max_length=3)),
                ('areaBelongingTo', models.CharField(max_length=50)),
                ('mailingAddress', models.CharField(max_length=150)),
                ('mailingPin', models.IntegerField(max_length=7)),
                ('mailingTelephone', models.IntegerField(max_length=11)),
                ('mailingMobile', models.IntegerField(max_length=11)),
                ('mailingPoliceStation', models.CharField(max_length=50)),
                ('permanentAddress', models.CharField(max_length=150)),
                ('permanentPin', models.IntegerField(max_length=7)),
                ('permanentTelephone', models.IntegerField(max_length=11)),
                ('permanentMobile', models.IntegerField(max_length=11)),
                ('permanentPoliceStation', models.CharField(max_length=50)),
                ('motherTongue', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('nativeState', models.CharField(max_length=20)),
                ('passportNo', models.IntegerField(max_length=7)),
                ('qualifyingExam', models.CharField(max_length=50)),
                ('qualifyingYear', models.IntegerField(max_length=7)),
                ('qualifyingBoard', models.CharField(max_length=50)),
                ('qualifyingPercentageMarks', models.IntegerField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('rollNumber', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=64)),
                ('emailId', models.EmailField(max_length=254)),
                ('hostelAlloted', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studentbiodatatable',
            name='uId',
            field=models.ForeignKey(to='sessionapp.UserList'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='roompreference',
            name='uId',
            field=models.ForeignKey(to='sessionapp.UserList'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friendspreference',
            name='uId',
            field=models.ForeignKey(to='sessionapp.UserList'),
            preserve_default=True,
        ),
    ]
