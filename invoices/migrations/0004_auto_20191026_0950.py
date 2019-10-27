# Generated by Django 2.2.4 on 2019-10-26 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_invoice_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice'),
            preserve_default=False,
        ),
    ]
