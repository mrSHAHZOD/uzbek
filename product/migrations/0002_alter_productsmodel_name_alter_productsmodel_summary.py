# Generated by Django 4.2.2 on 2023-07-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='summary',
            field=models.CharField(max_length=255),
        ),
    ]