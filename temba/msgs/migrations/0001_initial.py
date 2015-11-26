# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import temba.utils.models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
        ('schedules', '0001_initial'),
        ('channels', '0001_initial'),
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipient_count', models.IntegerField(help_text='Number of contacts to receive this broadcast', null=True, verbose_name='Number of recipients')),
                ('text', models.TextField(help_text='The message to send out', max_length=640, verbose_name='Text')),
                ('status', models.CharField(default='I', help_text='The current status for this broadcast', max_length=1, verbose_name='Status', choices=[('I', 'Initializing'), ('P', 'Pending'), ('Q', 'Queued'), ('W', 'Wired'), ('S', 'Sent'), ('D', 'Delivered'), ('H', 'Handled'), ('E', 'Error Sending'), ('F', 'Failed Sending'), ('R', 'Resent message')])),
                ('language_dict', models.TextField(help_text='The localized versions of the broadcast', null=True, verbose_name='Translations')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this broadcast is active')),
                ('created_on', models.DateTimeField(help_text='When this broadcast was created', auto_now_add=True, db_index=True)),
                ('modified_on', models.DateTimeField(help_text='When this item was last modified', auto_now=True)),
                ('channel', models.ForeignKey(verbose_name='Channel', to='channels.Channel', help_text='Channel to use for message sending', null=True)),
                ('contacts', models.ManyToManyField(help_text='Individual contacts included in this message', to='contacts.Contact', verbose_name='Contacts')),
                ('created_by', models.ForeignKey(related_name='msgs_broadcast_creations', to=settings.AUTH_USER_MODEL, help_text='The user which originally created this item')),
                ('groups', models.ManyToManyField(help_text='The groups to send the message to', to='contacts.ContactGroup', verbose_name='Groups')),
                ('modified_by', models.ForeignKey(related_name='msgs_broadcast_modifications', to=settings.AUTH_USER_MODEL, help_text='The user which last modified this item')),
                ('org', models.ForeignKey(verbose_name='Org', to='orgs.Org', help_text='The org this broadcast is connected to')),
                ('parent', models.ForeignKey(related_name='children', verbose_name='Parent', to='msgs.Broadcast', null=True)),
                ('schedule', models.OneToOneField(related_name='broadcast', null=True, to='schedules.Schedule', help_text='Our recurring schedule if we have one', verbose_name='Schedule')),
                ('urns', models.ManyToManyField(help_text='Individual URNs included in this message', to='contacts.ContactURN', verbose_name='URNs')),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('time', models.DateTimeField(help_text='When this call took place', verbose_name='Time')),
                ('duration', models.IntegerField(default=0, help_text='The duration of this call in seconds, if appropriate', verbose_name='Duration')),
                ('call_type', models.CharField(help_text='The type of call', max_length=16, verbose_name='Call Type', choices=[('unk', 'Unknown Call Type'), ('mo_call', 'Incoming Call'), ('mo_miss', 'Missed Incoming Call'), ('mt_call', 'Outgoing Call'), ('mt_miss', 'Missed Outgoing Call')])),
                ('channel', models.ForeignKey(verbose_name='Channel', to='channels.Channel', help_text='The channel where this call took place', null=True)),
                ('contact', models.ForeignKey(related_name='calls', verbose_name='Contact', to='contacts.Contact', help_text='The phone number for this call')),
                ('created_by', models.ForeignKey(related_name='msgs_call_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='msgs_call_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
                ('org', models.ForeignKey(verbose_name='Org', to='orgs.Org', help_text='The org this call is connected to')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExportMessagesTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('start_date', models.DateField(help_text='The date for the oldest message to export', null=True, blank=True)),
                ('end_date', models.DateField(help_text='The date for the newest message to export', null=True, blank=True)),
                ('host', models.CharField(help_text='The host this export task was created on', max_length=32)),
                ('task_id', models.CharField(max_length=64, null=True)),
                ('is_finished', models.BooleanField(default=False, help_text='Whether this export is finished running')),
                ('uuid', models.CharField(help_text='The uuid used to name the resulting export file', max_length=36, null=True)),
                ('created_by', models.ForeignKey(related_name='msgs_exportmessagestask_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('groups', models.ManyToManyField(to='contacts.ContactGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('uuid', models.CharField(default=temba.utils.models.generate_uuid, max_length=36, help_text='The unique identifier for this object', unique=True, verbose_name='Unique Identifier', db_index=True)),
                ('name', models.CharField(help_text='The name of this label', max_length=64, verbose_name='Name')),
                ('label_type', models.CharField(default='L', help_text='Label type', max_length=1, choices=[('F', 'Folder of labels'), ('L', 'Regular label')])),
                ('visible_count', models.PositiveIntegerField(default=0, help_text='Number of non-archived messages with this label')),
                ('created_by', models.ForeignKey(related_name='msgs_label_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('folder', models.ForeignKey(related_name='children', verbose_name='Folder', to='msgs.Label', null=True)),
                ('modified_by', models.ForeignKey(related_name='msgs_label_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
                ('org', models.ForeignKey(to='orgs.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(help_text='The actual message content that was sent', max_length=640, verbose_name='Text')),
                ('priority', models.IntegerField(default=500, help_text='The priority for this message to be sent, higher is higher priority')),
                ('created_on', models.DateTimeField(help_text='When this message was created', verbose_name='Created On', db_index=True)),
                ('sent_on', models.DateTimeField(help_text='When this message was sent to the endpoint', null=True, verbose_name='Sent On', blank=True)),
                ('delivered_on', models.DateTimeField(help_text='When this message was delivered to the final recipient (for incoming messages, when the message was handled)', null=True, verbose_name='Delivered On', blank=True)),
                ('queued_on', models.DateTimeField(help_text='When this message was queued to be sent or handled.', null=True, verbose_name='Queued On', blank=True)),
                ('direction', models.CharField(help_text='The direction for this message, either incoming or outgoing', max_length=1, verbose_name='Direction', choices=[('I', 'Incoming'), ('O', 'Outgoing')])),
                ('status', models.CharField(default='P', choices=[('I', 'Initializing'), ('P', 'Pending'), ('Q', 'Queued'), ('W', 'Wired'), ('S', 'Sent'), ('D', 'Delivered'), ('H', 'Handled'), ('E', 'Error Sending'), ('F', 'Failed Sending'), ('R', 'Resent message')], max_length=1, help_text='The current status for this message', verbose_name='Status', db_index=True)),
                ('visibility', models.CharField(default='V', choices=[('V', 'Visible'), ('A', 'Archived'), ('D', 'Deleted')], max_length=1, help_text='The current visibility of this message, either visible, archived or deleted', verbose_name='Visibility', db_index=True)),
                ('has_template_error', models.BooleanField(default=False, help_text='Whether data for variable substitution are missing', verbose_name='Has Template Error')),
                ('msg_type', models.CharField(help_text='The type of this message', max_length=1, null=True, verbose_name='Message Type', choices=[('I', 'Inbox Message'), ('F', 'Flow Message'), ('V', 'IVR Message')])),
                ('msg_count', models.IntegerField(default=1, help_text='The number of messages that were used to send this message, calculated on Twilio channels', verbose_name='Message Count')),
                ('error_count', models.IntegerField(default=0, help_text='The number of times this message has errored', verbose_name='Error Count')),
                ('next_attempt', models.DateTimeField(help_text='When we should next attempt to deliver this message', verbose_name='Next Attempt', auto_now_add=True)),
                ('external_id', models.CharField(max_length=255, blank=True, help_text='External id used for integrating with callbacks from other APIs', null=True, verbose_name='External ID', db_index=True)),
                ('recording_url', models.URLField(help_text='The url for any recording associated with this message', max_length=255, null=True, blank=True)),
                ('broadcast', models.ForeignKey(related_name='msgs', blank=True, to='msgs.Broadcast', help_text='If this message was sent to more than one recipient', null=True, verbose_name='Broadcast')),
                ('channel', models.ForeignKey(related_name='msgs', verbose_name='Channel', to='channels.Channel', help_text='The channel object that this message is associated with', null=True)),
                ('contact', models.ForeignKey(related_name='msgs', verbose_name='Contact', to='contacts.Contact', help_text='The contact this message is communicating with')),
                ('contact_urn', models.ForeignKey(related_name='msgs', verbose_name='Contact URN', to='contacts.ContactURN', help_text='The URN this message is communicating with', null=True)),
                ('labels', models.ManyToManyField(help_text='Any labels on this message', related_name='msgs', verbose_name='Labels', to='msgs.Label')),
                ('org', models.ForeignKey(related_name='msgs', verbose_name='Org', to='orgs.Org', help_text='The org this message is connected to')),
                ('response_to', models.ForeignKey(related_name='responses', blank=True, to='msgs.Msg', help_text='The message that this message is in reply to', null=True, verbose_name='Response To')),
                ('topup', models.ForeignKey(related_name='msgs', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='orgs.TopUp', help_text='The topup that this message was deducted from', null=True)),
            ],
            options={
                'ordering': ['-created_on', '-pk'],
            },
        ),
        migrations.CreateModel(
            name='SystemLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label_type', models.CharField(max_length=1, choices=[('I', 'Inbox'), ('W', 'Flows'), ('A', 'Archived'), ('O', 'Outbox'), ('S', 'Sent'), ('X', 'Failed'), ('E', 'Scheduled'), ('C', 'Calls')])),
                ('count', models.IntegerField(default=0, help_text='Number of items with this system label')),
                ('org', models.ForeignKey(related_name='system_labels', to='orgs.Org')),
            ],
        ),
        migrations.AddField(
            model_name='exportmessagestask',
            name='label',
            field=models.ForeignKey(to='msgs.Label', null=True),
        ),
        migrations.AddField(
            model_name='exportmessagestask',
            name='modified_by',
            field=models.ForeignKey(related_name='msgs_exportmessagestask_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='exportmessagestask',
            name='org',
            field=models.ForeignKey(help_text='The organization of the user.', to='orgs.Org'),
        ),
        migrations.AlterIndexTogether(
            name='systemlabel',
            index_together=set([('org', 'label_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='label',
            unique_together=set([('org', 'name')]),
        ),
    ]
