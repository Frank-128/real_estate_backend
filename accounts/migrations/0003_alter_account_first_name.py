# Generated by Django 4.2.4 on 2023-08-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_is_active_remove_account_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
    ]
