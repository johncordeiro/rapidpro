# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import temba.utils.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('uuid', models.CharField(default=temba.utils.models.generate_uuid, max_length=36, help_text='The unique identifier for this object', unique=True, verbose_name='Unique Identifier', db_index=True)),
                ('name', models.CharField(help_text='The name of this contact', max_length=128, null=True, verbose_name='Name', blank=True)),
                ('is_blocked', models.BooleanField(default=False, help_text='Whether this contact has been blocked', verbose_name='Is Blocked')),
                ('is_test', models.BooleanField(default=False, help_text='Whether this contact is for simulation', verbose_name='Is Test')),
                ('is_failed', models.BooleanField(default=False, help_text='Whether we cannot send messages to this contact', verbose_name='Is Failed')),
                ('language', models.CharField(help_text='The preferred language for this contact', max_length=3, null=True, verbose_name='Language', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=36, verbose_name='Label')),
                ('key', models.CharField(max_length=36, verbose_name='Key')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('value_type', models.CharField(default='T', max_length=1, verbose_name='Field Type', choices=[('T', 'Text'), ('N', 'Numeric'), ('D', 'Date & Time'), ('S', 'State'), ('I', 'District')])),
                ('show_in_table', models.BooleanField(default=False, verbose_name='Shown in Tables')),
            ],
        ),
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('uuid', models.CharField(default=temba.utils.models.generate_uuid, max_length=36, help_text='The unique identifier for this object', unique=True, verbose_name='Unique Identifier', db_index=True)),
                ('name', models.CharField(help_text='The name of this contact group', max_length=64, verbose_name='Name')),
                ('group_type', models.CharField(default='U', help_text='What type of group it is, either user defined or one of our system groups', max_length=1, choices=[('A', 'All Contacts'), ('B', 'Blocked Contacts'), ('F', 'Failed Contacts'), ('U', 'User Defined Groups')])),
                ('count', models.IntegerField(default=0, help_text='The number of contacts in this group', verbose_name='Count')),
                ('query', models.TextField(help_text='The membership query for this group', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactURN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('urn', models.CharField(help_text='The Universal Resource Name as a string. ex: tel:+250788383383', max_length=255, choices=[('tel', 'Phone number'), ('twitter', 'Twitter handle'), ('ext', 'External identifier')])),
                ('path', models.CharField(help_text='The path component of our URN. ex: +250788383383', max_length=255)),
                ('scheme', models.CharField(help_text='The scheme for this URN, broken out for optimization reasons, ex: tel', max_length=128)),
                ('priority', models.IntegerField(default=50, help_text='The priority of this URN for the contact it is associated with')),
            ],
            options={
                'ordering': ('-priority', 'id'),
            },
        ),
        migrations.CreateModel(
            name='ExportContactsTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('host', models.CharField(help_text='The host this export task was created on', max_length=32)),
                ('task_id', models.CharField(max_length=64, null=True)),
                ('is_finished', models.BooleanField(default=False, help_text='Whether this export has completed')),
                ('uuid', models.CharField(help_text='The uuid used to name the resulting export file', max_length=36, null=True)),
                ('created_by', models.ForeignKey(related_name='contacts_exportcontactstask_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('group', models.ForeignKey(related_name='exports', to='contacts.ContactGroup', help_text='The unique group to export', null=True)),
                ('modified_by', models.ForeignKey(related_name='contacts_exportcontactstask_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
