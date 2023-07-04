# Generated by Django 4.2.2 on 2023-06-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]