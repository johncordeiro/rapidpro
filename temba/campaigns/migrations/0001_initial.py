# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import temba.utils.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('name', models.CharField(help_text='The name of this campaign', max_length=255)),
                ('is_archived', models.BooleanField(default=False, help_text='Whether this campaign is archived or not')),
                ('uuid', models.CharField(default=temba.utils.models.generate_uuid, help_text='The unique identifier for this object', unique=True, max_length=36, verbose_name='Unique Identifier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampaignEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('offset', models.IntegerField(default=0, help_text='The offset in days from our date (positive is after, negative is before)')),
                ('unit', models.CharField(default='D', help_text='The unit for the offset for this event', max_length=1, choices=[('M', 'Minutes'), ('H', 'Hours'), ('D', 'Days'), ('W', 'Weeks')])),
                ('event_type', models.CharField(default='F', help_text='The type of this event', max_length=1, choices=[('F', 'Flow Event'), ('M', 'Message Event')])),
                ('message', models.TextField(help_text='The message to send out', null=True, blank=True)),
                ('delivery_hour', models.IntegerField(default=-1, help_text='The hour to send the message or flow at.')),
                ('uuid', models.CharField(default=temba.utils.models.generate_uuid, help_text='The unique identifier for this object', unique=True, max_length=36, verbose_name='Unique Identifier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventFire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scheduled', models.DateTimeField(help_text='When this event is scheduled to run')),
                ('fired', models.DateTimeField(help_text='When this event actually fired, null if not yet fired', null=True, blank=True)),
            ],
            options={
                'ordering': ('scheduled',),
            },
        ),
    ]
