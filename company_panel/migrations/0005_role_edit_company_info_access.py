# Generated by Django 2.2.4 on 2019-11-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_panel', '0004_role_kick_user_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='edit_company_info_access',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
