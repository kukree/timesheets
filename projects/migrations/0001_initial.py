# Generated by Django 2.2.4 on 2019-11-05 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manage_app', '0001_initial'),
        ('company_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('notes', models.CharField(blank=True, default=' ', max_length=350)),
                ('budget', models.FloatField()),
                ('total_earned', models.FloatField(default=0)),
                ('total_spent', models.FloatField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='manage_app.Client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='company_panel.Company')),
                ('tasks', models.ManyToManyField(to='manage_app.Task')),
            ],
        ),
    ]
