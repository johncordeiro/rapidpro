# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('msgs', '0001_initial'),
        ('channels', '0001_initial'),
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channellog',
            name='msg',
            field=models.ForeignKey(help_text='The message that was sent', to='msgs.Msg'),
        ),
        migrations.AddField(
            model_name='channelcount',
            name='channel',
            field=models.ForeignKey(help_text='The channel this is a daily summary count for', to='channels.Channel'),
        ),
        migrations.AddField(
            model_name='channel',
            name='created_by',
            field=models.ForeignKey(related_name='channels_channel_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='channel',
            name='modified_by',
            field=models.ForeignKey(related_name='channels_channel_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='channel',
            name='org',
            field=models.ForeignKey(related_name='channels', blank=True, to='orgs.Org', help_text='Organization using this channel', null=True, verbose_name='Org'),
        ),
        migrations.AddField(
            model_name='channel',
            name='parent',
            field=models.ForeignKey(blank=True, to='channels.Channel', help_text='The channel this channel is working on behalf of', null=True),
        ),
        migrations.AddField(
            model_name='alert',
            name='channel',
            field=models.ForeignKey(verbose_name='Channel', to='channels.Channel', help_text='The channel that this alert is for'),
        ),
        migrations.AddField(
            model_name='alert',
            name='created_by',
            field=models.ForeignKey(related_name='channels_alert_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='alert',
            name='modified_by',
            field=models.ForeignKey(related_name='channels_alert_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='alert',
            name='sync_event',
            field=models.ForeignKey(verbose_name='Sync Event', to='channels.SyncEvent', help_text='The sync event that caused this alert to be sent (if any)', null=True),
        ),
        migrations.AlterIndexTogether(
            name='channelcount',
            index_together=set([('channel', 'count_type', 'day')]),
        ),
    ]
