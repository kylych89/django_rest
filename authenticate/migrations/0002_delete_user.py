# Generated by Django 4.1.5 on 2023-01-17 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]