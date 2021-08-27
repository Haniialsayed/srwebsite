from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('survey', views.survey, name='survey'),
    path('selection', views.collect_methods, name='collect_methods'),
    path('recommend', views.pass_recommendation, name="recommendations"),
    path('search', views.search_slug, name="search")
]
