# Generated by Django 2.2.4 on 2019-11-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_panel', '0005_role_edit_company_info_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='manage_roles_access',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]