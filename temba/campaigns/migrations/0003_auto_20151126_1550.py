# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flows', '0001_initial'),
        ('contacts', '0001_initial'),
        ('campaigns', '0002_auto_20151126_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignevent',
            name='flow',
            field=models.ForeignKey(help_text='The flow that will be triggered', to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='campaignevent',
            name='modified_by',
            field=models.ForeignKey(related_name='campaigns_campaignevent_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
        migrations.AddField(
            model_name='campaignevent',
            name='relative_to',
            field=models.ForeignKey(related_name='campaigns', to='contacts.ContactField', help_text='The field our offset is relative to'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='created_by',
            field=models.ForeignKey(related_name='campaigns_campaign_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='group',
            field=models.ForeignKey(help_text='The group this campaign operates on', to='contacts.ContactGroup'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='modified_by',
            field=models.ForeignKey(related_name='campaigns_campaign_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item'),
        ),
    ]
