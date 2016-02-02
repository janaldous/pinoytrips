# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='operator',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
