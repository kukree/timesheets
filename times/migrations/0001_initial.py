# Generated by Django 2.2.4 on 2019-09-29 11:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_panel', '0001_initial'),
        ('manage_app', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2019, 9, 29))),
                ('notes', models.CharField(blank=True, default=' ', max_length=350)),
                ('timer', models.TimeField(default=datetime.time(0, 0))),
                ('start_time', models.TimeField(default=datetime.time(0, 0))),
                ('is_active', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_panel.Company')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_app.Task')),
            ],
        ),
    ]
