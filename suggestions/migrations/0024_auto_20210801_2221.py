# Generated by Django 3.2.3 on 2021-08-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0023_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_one', models.CharField(max_length=20)),
                ('check_two', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Select',
        ),
    ]