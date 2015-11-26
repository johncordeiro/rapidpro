# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivr', '0001_initial'),
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ivrcall',
            name='org',
            field=models.ForeignKey(help_text='The organization this call belongs to', to='orgs.Org'),
        ),
    ]
