# Generated by Django 2.2.4 on 2019-11-05 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_own', to=settings.AUTH_USER_MODEL),
        ),
    ]
