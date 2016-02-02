# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0002_auto_20150511_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='operator',
            name='rating',
            field=models.CharField(default=b'Non-ac', max_length=10),
        ),
    ]
