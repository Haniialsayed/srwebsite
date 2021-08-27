from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from suggestions.models import Method

from .forms import SignUpForm
from .models import Survey, Selection, Recommendation, StressLevel

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import random
from recommendations.recommender import initial, get_stress_reduction_method, get_stress_reduction_recommendation, \
    change_recommendations, remove_bad_data, next_similarity


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home2')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #  log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('home2')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")


def survey(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', 'None')
        last_name = request.POST.get('last_name', 'None')
        gender = request.POST.get('gender', 'None')
        age = request.POST.get('age', 'None')
        weight = request.POST.get('weight', 'None')
        height = request.POST.get('height', 'None')
        work_hours = request.POST.get('work_hours', 'None')
        job_role = request.POST.get('job_role', 'None')
        address = request.POST.get('address', 'None')
        address_2 = request.POST.get('address2', 'None')
        country = request.POST.get('country', 'None')
        city = request.POST.get('city', 'None')
        state = request.POST.get('state', 'None')
        zip_code = request.POST.get('zip', 'None')
        Survey(first_name=first_name,
               last_name=last_name,
               gender=gender,
               age=age,
               weight=weight,
               height=height,
               work_hours=work_hours,
               job_role=job_role,
               address=address,
               address_2=address_2,
               country=country,
               city=city,
               state=state,
               zip_code=zip_code).save()
        return redirect('methods:list')
    else:
        return render(request, 'accounts/survey.html')


@login_required(login_url="/accounts/login/")
def collect_methods(request):
    if request.method == "POST":
        drink_enough_water = request.POST.get('drink_enough_water', 1)
        take_a_walk = request.POST.get('take_a_walk', 1)
        laugh_more = request.POST.get('laugh_more', 1)
        do_some_meditation = request.POST.get('do_some_meditation', 1)
        get_support_from_colleagues = request.POST.get('get_support_from_colleagues', 1)
        avoid_smoking_and_nicotine = request.POST.get('avoid_smoking_and_nicotine', 1)
        avoid_procrastinating = request.POST.get('avoid_procrastinating', 1)
        practice_deep_breathing = request.POST.get('practice_deep_breathing', 1)
        do_some_yoga = request.POST.get('do_some_yoga', 1)
        engage_your_social_support_group = request.POST.get('engage_your_social_support_group', 1)
        listen_to_soothing_music = request.POST.get('listen_to_soothing_music', 1)
        take_some_yoghurt = request.POST.get('take_some_yoghurt', 1)
        eat_enough_eggs = request.POST.get('eat_enough_eggs', 1)
        take_green_tea_supplements = request.POST.get('take_green_tea_supplements', 1)
        eat_some_turkey = request.POST.get('eat_some_turkey', 1)
        take_some_oatmeal = request.POST.get('take_some_oatmeal', 1)
        eat_more_vegetables = request.POST.get('eat_more_vegetables', 1)
        eat_some_citrus_fruits_like_oranges = request.POST.get('eat_some_citrus_fruits_like_oranges', 1)
        pray_more = request.POST.get('pray_more', 1)
        take_a_vacation = request.POST.get('take_a_vacation', 1)
        sleep_well = request.POST.get('sleep_well', 1)
        reduce_your_caffeine_intake = request.POST.get('reduce_your_caffeine_intake', 1)
        avoid_overworking_yourself = request.POST.get('avoid_overworking_yourself', 1)
        avoid_negativity = request.POST.get('avoid_negativity', 1)
        Selection(drink_enough_water=drink_enough_water,
                  take_a_walk=take_a_walk,
                  laugh_more=laugh_more,
                  do_some_meditation=do_some_meditation,
                  get_support_from_colleagues=get_support_from_colleagues,
                  avoid_smoking_and_nicotine=avoid_smoking_and_nicotine,
                  avoid_procrastinating=avoid_procrastinating,
                  practice_deep_breathing=practice_deep_breathing,
                  do_some_yoga=do_some_yoga,
                  engage_your_social_support_group=engage_your_social_support_group,
                  listen_to_soothing_music=listen_to_soothing_music,
                  take_some_yoghurt=take_some_yoghurt,
                  eat_enough_eggs=eat_enough_eggs,
                  take_green_tea_supplements=take_green_tea_supplements,
                  eat_some_turkey=eat_some_turkey,
                  take_some_oatmeal=take_some_oatmeal,
                  eat_more_vegetables=eat_more_vegetables,
                  eat_some_citrus_fruits_like_oranges=eat_some_citrus_fruits_like_oranges,
                  pray_more=pray_more,
                  take_a_vacation=take_a_vacation,
                  sleep_well=sleep_well,
                  reduce_your_caffeine_intake=reduce_your_caffeine_intake,
                  avoid_overworking_yourself=avoid_overworking_yourself,
                  avoid_negativity=avoid_negativity).save()
        method_list = ['drink_enough_water', 'take_a_walk', 'laugh_more', 'do_some_meditation',
                       'get_support_from_colleagues', 'avoid_smoking_and_nicotine', 'avoid_procrastinating',
                       'practice_deep_breathing', 'do_some_yoga', 'engage_your_social_support_group',
                       'listen_to_soothing_music', 'take_some_yoghurt', 'eat_enough_eggs',
                       'take_green_tea_supplements', 'eat_some_turkey', 'take_some_oatmeal',
                       'eat_more_vegetables', 'eat_some_citrus_fruits_like_oranges', 'pray_more',
                       'take_a_vacation', 'sleep_well', 'reduce_your_caffeine_intake',
                       'avoid_overworking_yourself', 'avoid_negativity']
        methods_list = ['Drinking 3 litres of water daily', 'Taking a walk', 'laughter', 'Meditation',
                        'Talking to your colleague', 'Avoid Tobacco and nicotine', 'Avoiding Procrastination',
                        'Deep Breating', 'Yoga', 'Taking a break to relax',
                        # 'Taking a break to relax should be Engage your support group',
                        'Listening to music', 'Taking Yoghurt', 'Eating Eggs', 'Taking Green Tea supplement',
                        'Eating Turkey', 'Taking Oatmeal', 'Eating Vegetables',
                        'Eating Citrus Fruits like Oranges and Grapefruit', 'Prayer', 'Taking time off', 'Sleep well',
                        'Avoiding Caffeine', "Don't work more than 7 hours", 'Avoid Negativity']
        rate_list = []
        for method in method_list:
            generator_list = Selection.objects.values_list(method).iterator()  # get all the collection of all rate values
            user_selection = list([i for i in generator_list][-1])  # iterate over them one by one and append them to list
            rate_list.append(user_selection[0])
        rate_list = [int(i) for i in rate_list]
        selection_dict = dict(zip(methods_list, rate_list))
        selection_dict = remove_bad_data(selection_dict)
        selection_list = list(selection_dict.items())
        # print(f'This is the selection list: {selection_list}')

        stress_object = StressLevel.objects.latest('date')
        stress_value = stress_object.level
        ratings, user_similarity_df = initial()
        num = random.randint(1, 38)
        user = f"User {num}"
        similar_users = get_stress_reduction_method(user=user, stress_value=stress_value,
                                                    user_similarity_df=user_similarity_df)
        users = similar_users.index.values.tolist()
        item_similarity_df = next_similarity(ratings=ratings, users=users)
        similar_method = pd.DataFrame()
        for method, rating in selection_list:
            similar_method = similar_method.append(get_stress_reduction_recommendation(method, rating,
                                                                                       item_similarity_df),
                                                   ignore_index=True)
        recommend_dataframe = similar_method.sum().sort_values(ascending=False)
        recommend_method = recommend_dataframe.index.tolist()[:5]
        recommendations = change_recommendations(recommend_method)
        recommendation_1 = recommendations[0]
        recommendation_2 = recommendations[1]
        recommendation_3 = recommendations[2]
        recommendation_4 = recommendations[3]
        recommendation_5 = recommendations[4]
        Recommendation(recommendation_1=recommendation_1,
                       recommendation_2=recommendation_2,
                       recommendation_3=recommendation_3,
                       recommendation_4=recommendation_4,
                       recommendation_5=recommendation_5).save()
        return redirect('accounts:recommendations')
    else:
        return render(request, 'methods:list')


@login_required(login_url="/accounts/login/")
def pass_recommendation(request):
    post_recommendations = Recommendation.objects.latest('date')
    return render(request, 'recommend.html', {'post_recommendations': post_recommendations})


@login_required(login_url="/accounts/login/")
def search_slug(request):
    if request.method == "POST":
        data = request.POST['search']
        data = data.replace(" ", "-").lower()
        suggestion = Method.objects.get(slug=data)
        return render(request, "suggestions/suggestion_detail.html", {"suggestion": suggestion})
