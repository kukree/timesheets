# Generated by Django 3.0.8 on 2020-08-18 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200809_1831'),
        ('invoices', '0003_auto_20200809_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='unit_price',
        ),
        migrations.AddField(
            model_name='item',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='projects.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoices.Invoice'),
        ),
    ]