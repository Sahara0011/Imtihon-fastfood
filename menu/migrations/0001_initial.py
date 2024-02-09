# Generated by Django 5.0.2 on 2024-02-08 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.FloatField(default=0)),
                ('image', models.ImageField(upload_to='product/')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.producttype')),
            ],
        ),
    ]