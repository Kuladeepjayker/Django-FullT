# Generated by Django 3.0.6 on 2020-07-03 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FThrottle', '0002_employees_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 3, 15, 0, 29, 93636)),
        ),
    ]
