# Generated by Django 3.2.3 on 2021-07-22 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0013_createemployee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createemployee',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='createemployee',
            old_name='zip',
            new_name='zip_code',
        ),
        migrations.RemoveField(
            model_name='createemployee',
            name='email',
        ),
    ]
