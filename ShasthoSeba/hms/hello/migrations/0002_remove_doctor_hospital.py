# Generated by Django 4.2.1 on 2023-06-03 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='hospital',
        ),
    ]
