# Generated by Django 5.1.3 on 2024-11-15 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model']},
        ),
    ]
