# Generated by Django 2.2.4 on 2019-12-07 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_panel', '0009_auto_20191125_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date_of_creation',
            field=models.DateField(default=datetime.date(2019, 12, 7)),
        ),
    ]
