from django.shortcuts import render, redirect
from suggestions.models import Method
from django.contrib.auth.decorators import login_required
from accounts.models import Recommendation
from recommendations.recommender import recommend_frontpage
from accounts.models import StressLevel


def homepage(request):
    return render(request, 'homepage.html')


@login_required(login_url="/accounts/login/")
def homepage2(request):
    current_user = request.user
    post_recommendations = Recommendation.objects.latest('date')
    recommendation_1 = recommend_frontpage(post_recommendations.recommendation_1)
    recommendation_2 = recommend_frontpage(post_recommendations.recommendation_2)
    recommendation_3 = recommend_frontpage(post_recommendations.recommendation_3)
    recommendation_4 = recommend_frontpage(post_recommendations.recommendation_4)
    recommendation_5 = recommend_frontpage(post_recommendations.recommendation_5)
    return render(request, 'homepage2.html', {'current_user': current_user,
                                              'recommendation_1': recommendation_1,
                                              'recommendation_2': recommendation_2,
                                              'recommendation_3': recommendation_3,
                                              'recommendation_4': recommendation_4,
                                              'recommendation_5': recommendation_5})


def about(request):
    return render(request, 'about.html')


@login_required(login_url="/accounts/login/")
def stress_level(request):
    if request.method == "POST":
        level = request.POST.get('s_level', 5)
        StressLevel(level=level).save()
        return render(request, 'about.html')


def test(request):
    methods = Method.objects.all()
    return render(request, 'test.html', {'methods': methods})

