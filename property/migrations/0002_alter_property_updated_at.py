# Generated by Django 4.2.4 on 2023-08-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
