from django.contrib import admin
from .models import Survey, Selection, Recommendation, StressLevel


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'age', 'weight', 'height', 'work_hours', 'job_role', 'address',
                    'address_2', 'country', 'city', 'state', 'zip_code')


class SelectionAdmin(admin.ModelAdmin):
    list_display = ('drink_enough_water', 'take_a_walk', 'laugh_more', 'do_some_meditation',
                    'get_support_from_colleagues', 'avoid_smoking_and_nicotine', 'avoid_procrastinating',
                    'practice_deep_breathing', 'do_some_yoga', 'engage_your_social_support_group',
                    'listen_to_soothing_music', 'take_some_yoghurt', 'eat_enough_eggs', 'take_green_tea_supplements',
                    'eat_some_turkey', 'take_some_oatmeal', 'eat_more_vegetables',
                    'eat_some_citrus_fruits_like_oranges', 'pray_more', 'take_a_vacation', 'sleep_well',
                    'reduce_your_caffeine_intake', 'avoid_overworking_yourself', 'avoid_negativity')


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('recommendation_1', 'recommendation_2', 'recommendation_3', 'recommendation_4', 'recommendation_5',
                    'date')


class StressLevelAdmin(admin.ModelAdmin):
    list_display = ('level', 'date')


# we need to register our models here to enable django show them in the admin page.
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Selection, SelectionAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(StressLevel, StressLevelAdmin)
