# Generated by Django 3.2.3 on 2021-08-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210814_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stresslevel',
            name='level',
            field=models.IntegerField(),
        ),
    ]
