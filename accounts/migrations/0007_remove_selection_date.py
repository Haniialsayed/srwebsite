# Generated by Django 3.2.3 on 2021-08-03 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_delete_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selection',
            name='date',
        ),
    ]
