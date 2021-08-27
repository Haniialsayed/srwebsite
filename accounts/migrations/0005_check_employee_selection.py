# Generated by Django 3.2.3 on 2021-08-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_survey_id'),
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
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_enough_water', models.CharField(default='None', max_length=50)),
                ('take_a_walk', models.CharField(default='None', max_length=50)),
                ('laugh_more', models.CharField(default='None', max_length=50)),
                ('do_some_meditation', models.CharField(default='None', max_length=50)),
                ('get_support_from_colleagues', models.CharField(default='None', max_length=50)),
                ('avoid_smoking_and_nicotine', models.CharField(default='None', max_length=50)),
                ('avoid_procrastinating', models.CharField(default='None', max_length=50)),
                ('practice_deep_breathing', models.CharField(default='None', max_length=50)),
                ('do_some_yoga', models.CharField(default='None', max_length=50)),
                ('engage_your_social_support_group', models.CharField(default='None', max_length=50)),
                ('listen_to_soothing_music', models.CharField(default='None', max_length=50)),
                ('take_some_yoghurt', models.CharField(default='None', max_length=50)),
                ('eat_enough_eggs', models.CharField(default='None', max_length=50)),
                ('take_green_tea_supplements', models.CharField(default='None', max_length=50)),
                ('eat_some_turkey', models.CharField(default='None', max_length=50)),
                ('take_some_oatmeal', models.CharField(default='None', max_length=50)),
                ('eat_more_vegetables', models.CharField(default='None', max_length=50)),
                ('eat_some_citrus_fruits_like_oranges', models.CharField(default='None', max_length=50)),
                ('pray_more', models.CharField(default='None', max_length=50)),
                ('take_a_vacation', models.CharField(default='None', max_length=50)),
                ('sleep_well', models.CharField(default='None', max_length=50)),
                ('reduce_your_caffeine_intake', models.CharField(default='None', max_length=50)),
                ('avoid_overworking_yourself', models.CharField(default='None', max_length=50)),
                ('avoid_negativity', models.CharField(default='None', max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]