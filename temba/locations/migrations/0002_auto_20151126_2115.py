# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boundaryalias',
            name='org',
            field=models.ForeignKey(help_text=b'The org that owns this alias', to='orgs.Org'),
        ),
        migrations.AddField(
            model_name='adminboundary',
            name='parent',
            field=models.ForeignKey(related_name='children', to='locations.AdminBoundary', help_text=b'The parent to this political boundary if any', null=True),
        ),
    ]
