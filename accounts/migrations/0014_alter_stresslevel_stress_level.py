# Generated by Django 3.2.3 on 2021-08-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_stresslevel_stress_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stresslevel',
            name='stress_level',
            field=models.IntegerField(),
        ),
    ]
