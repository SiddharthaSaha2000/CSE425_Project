# Generated by Django 4.2.1 on 2023-06-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_remove_doctor_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.CharField(default='', max_length=255),
        ),
    ]