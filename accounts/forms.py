from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class Survey(forms.ModelForm):
    class Meta:
        model = models.Survey
        fields = ['first_name', 'last_name', 'gender', 'age', 'weight', 'height', 'work_hours', 'job_role',
                  'address', 'address_2', 'country', 'city', 'state', 'zip_code']


class Selection(forms.ModelForm):
    class Meta:
        model = models.Selection
        fields = ['drink_enough_water', 'take_a_walk', 'laugh_more', 'do_some_meditation',
                  'get_support_from_colleagues', 'avoid_smoking_and_nicotine', 'avoid_procrastinating',
                  'practice_deep_breathing', 'do_some_yoga', 'engage_your_social_support_group',
                  'listen_to_soothing_music', 'take_some_yoghurt', 'eat_enough_eggs', 'take_green_tea_supplements',
                  'eat_some_turkey', 'take_some_oatmeal', 'eat_more_vegetables', 'eat_some_citrus_fruits_like_oranges',
                  'pray_more', 'take_a_vacation', 'sleep_well', 'reduce_your_caffeine_intake',
                  'avoid_overworking_yourself', 'avoid_negativity']


class Recommendation(forms.ModelForm):
    class Meta:
        model = models.Recommendation
        fields = ['recommendation_1', 'recommendation_2', 'recommendation_3', 'recommendation_4', 'recommendation_5']


class StressLevel(forms.ModelForm):
    class Meta:
        model = models.StressLevel
        fields = ['level']
