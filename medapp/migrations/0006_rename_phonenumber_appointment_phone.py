# Generated by Django 5.1.6 on 2025-02-28 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0005_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='phonenumber',
            new_name='phone',
        ),
    ]
