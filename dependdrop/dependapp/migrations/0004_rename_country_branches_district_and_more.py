# Generated by Django 4.2 on 2023-04-17 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dependapp', '0003_rename_city_branches_rename_country_districts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branches',
            old_name='country',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='city',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='country',
            new_name='district',
        ),
    ]
