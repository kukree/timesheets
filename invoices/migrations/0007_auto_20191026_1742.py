# Generated by Django 2.2.4 on 2019-10-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_auto_20191026_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, default=' ', max_length=350),
        ),
    ]
