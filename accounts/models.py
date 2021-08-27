from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class Survey(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(default=0,
                              validators=[MaxValueValidator(100),
                                          MinValueValidator(0)
                                          ])
    weight = models.IntegerField(default=0,
                                 validators=[MaxValueValidator(100),
                                             MinValueValidator(0)
                                             ])
    height = models.IntegerField(default=0,
                                 validators=[MaxValueValidator(300),
                                             MinValueValidator(0)
                                             ])
    work_hours = models.IntegerField(default=0,
                                     validators=[MaxValueValidator(100),
                                                 MinValueValidator(0)
                                                 ])
    job_role = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    address_2 = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField(default=0,
                                   validators=[MaxValueValidator(1000000),
                                               MinValueValidator(0)
                                               ])


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Selection(models.Model):  # change this charfield to integerfield
    drink_enough_water = models.IntegerField()
    take_a_walk = models.IntegerField()
    laugh_more = models.IntegerField()
    do_some_meditation = models.IntegerField()
    get_support_from_colleagues = models.IntegerField()
    avoid_smoking_and_nicotine = models.IntegerField()
    avoid_procrastinating = models.IntegerField()
    practice_deep_breathing = models.IntegerField()
    do_some_yoga = models.IntegerField()
    engage_your_social_support_group = models.IntegerField()
    listen_to_soothing_music = models.IntegerField()
    take_some_yoghurt = models.IntegerField()
    eat_enough_eggs = models.IntegerField()
    take_green_tea_supplements = models.IntegerField()
    eat_some_turkey = models.IntegerField()
    take_some_oatmeal = models.IntegerField()
    eat_more_vegetables = models.IntegerField()
    eat_some_citrus_fruits_like_oranges = models.IntegerField()
    pray_more = models.IntegerField()
    take_a_vacation = models.IntegerField()
    sleep_well = models.IntegerField()
    reduce_your_caffeine_intake = models.IntegerField()
    avoid_overworking_yourself = models.IntegerField()
    avoid_negativity = models.IntegerField()
#    user = models.ForeignKey(Employee, on_delete=models.CASCADE, )
#    date = models.DateTimeField(auto_now_add=True)


class Recommendation(models.Model):
    recommendation_1 = models.CharField(max_length=500, default='None')
    recommendation_2 = models.CharField(max_length=500, default='None')
    recommendation_3 = models.CharField(max_length=500, default='None')
    recommendation_4 = models.CharField(max_length=500, default='None')
    recommendation_5 = models.CharField(max_length=500, default='None')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.recommendation_1,
                                   self.recommendation_2,
                                   self.recommendation_3,
                                   self.recommendation_4,
                                   self.recommendation_5)


class StressLevel(models.Model):
    level = models.IntegerField(default=5)
    date = models.DateTimeField(auto_now_add=True)
