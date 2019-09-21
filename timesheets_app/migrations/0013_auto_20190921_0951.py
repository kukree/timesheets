# Generated by Django 2.2.4 on 2019-09-21 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets_app', '0012_auto_20190921_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets_app.Company'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets_app.Company'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets_app.Task'),
        ),
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets_app.Company'),
        ),
        migrations.AlterField(
            model_name='task',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets_app.Company'),
        ),
    ]
