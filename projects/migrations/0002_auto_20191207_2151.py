# Generated by Django 2.2.4 on 2019-12-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='notes',
            field=models.TextField(blank=True, default=' ', max_length=350),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_earned',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_spent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
