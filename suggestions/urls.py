from django.urls import path
from . import views


app_name = "methods"

urlpatterns = [
    path('suggestion_list', views.suggestion_list, name="list"),
    path('<slug>', views.suggestion_detail, name="detail")
]
