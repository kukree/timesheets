# Generated by Django 2.2.4 on 2019-09-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets_app', '0016_auto_20190921_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='notes',
            field=models.CharField(blank=True, default=' ', max_length=350),
        ),
    ]