# Generated by Django 3.2.3 on 2021-08-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_recommendation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='StressLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stress_level', models.IntegerField()),
            ],
        ),
    ]