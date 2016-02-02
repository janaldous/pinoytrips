# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0003_auto_20150511_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='features',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='operator',
            name='rating',
            field=models.CharField(choices=[(b'non-ac', b'Non-airconditioned'), (b'ac', b'Airconditioned'), (b'business', b'Business')], default=b'Non-ac', max_length=10),
        ),
    ]
