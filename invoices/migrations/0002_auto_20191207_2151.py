# Generated by Django 2.2.4 on 2019-12-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='notes',
            field=models.TextField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
