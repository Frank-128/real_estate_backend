# Generated by Django 4.2.4 on 2023-08-24 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=15)),
                ('district', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'property_address',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attributes',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('estate_name', models.CharField(max_length=255)),
                ('conditions', models.CharField(max_length=255, null=True)),
                ('utilities', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(max_length=500)),
                ('is_for_sale', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'properties',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='PropertyAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'property_attributes',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='PropertyCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'property_categories',
            },
        ),
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.propertycategories', verbose_name='Property Category')),
            ],
            options={
                'db_table': 'property_types',
            },
        ),
        migrations.CreateModel(
            name='PropertyPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_picture', models.ImageField(height_field=40, null=True, upload_to='property_pictures', width_field=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user picture')),
            ],
            options={
                'db_table': 'property_pictures',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='propertycategories',
            index=models.Index(fields=['category_name'], name='property_ca_categor_8b0352_idx'),
        ),
        migrations.AddField(
            model_name='propertyattributes',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.attributes', verbose_name='Property Attribute'),
        ),
        migrations.AddField(
            model_name='propertyattributes',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property', verbose_name='Property Name'),
        ),
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.address', verbose_name='property address'),
        ),
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.propertycategories', verbose_name='property category'),
        ),
        migrations.AddField(
            model_name='property',
            name='pictures',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.propertypictures', verbose_name='property picture'),
        ),
        migrations.AddField(
            model_name='property',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.propertytypes', verbose_name='property type'),
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='property owner'),
        ),
        migrations.AddIndex(
            model_name='attributes',
            index=models.Index(fields=['attribute_name'], name='attributes_attribu_2f6666_idx'),
        ),
        migrations.AddIndex(
            model_name='address',
            index=models.Index(fields=['region', 'district', 'street'], name='property_ad_region_be3b9b_idx'),
        ),
        migrations.AddIndex(
            model_name='propertytypes',
            index=models.Index(fields=['type_name'], name='property_ty_type_na_46017d_idx'),
        ),
        migrations.AddIndex(
            model_name='propertyattributes',
            index=models.Index(fields=['attribute'], name='property_at_attribu_9879ea_idx'),
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['user', 'address'], name='properties_user_id_ceb993_idx'),
        ),
    ]
