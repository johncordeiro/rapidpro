# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flows', '0001_initial'),
        ('contacts', '0001_initial'),
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IVRCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('external_id', models.CharField(help_text='The external id for this call, our twilio id usually', max_length=255)),
                ('status', models.CharField(default='P', help_text='The status of this call', max_length=1, choices=[('Q', 'Queued'), ('R', 'Ringing'), ('I', 'In Progress'), ('D', 'Complete'), ('B', 'Busy'), ('F', 'Failed'), ('N', 'No Answer'), ('C', 'Canceled')])),
                ('direction', models.CharField(help_text='The direction of this call, either incoming or outgoing', max_length=1, choices=[('I', 'Incoming'), ('O', 'Outgoing')])),
                ('started_on', models.DateTimeField(help_text='When this call was connected and started', null=True, blank=True)),
                ('ended_on', models.DateTimeField(help_text='When this call ended', null=True, blank=True)),
                ('call_type', models.CharField(default='F', help_text='What sort of call is this', max_length=1, choices=[('F', 'Flow')])),
                ('duration', models.IntegerField(default=0, help_text='The length of this call in seconds', null=True)),
                ('channel', models.ForeignKey(help_text='The channel that made this call', to='channels.Channel')),
                ('contact', models.ForeignKey(help_text='Who this call is with', to='contacts.Contact')),
                ('contact_urn', models.ForeignKey(verbose_name='Contact URN', to='contacts.ContactURN', help_text='The URN this call is communicating with')),
                ('created_by', models.ForeignKey(related_name='ivr_ivrcall_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('flow', models.ForeignKey(to='flows.Flow', help_text='The flow this call was part of', null=True)),
                ('modified_by', models.ForeignKey(related_name='ivr_ivrcall_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
