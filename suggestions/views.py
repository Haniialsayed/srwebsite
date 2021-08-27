from django.shortcuts import render, redirect
from .models import Method
from django.contrib.auth.decorators import login_required
from . import forms
import pandas as pd


@login_required(login_url="/accounts/login/")
def suggestion_list(request):
    # this grabs all of the records from this method database table
    methods = Method.objects.all().order_by('name')
    return render(request, 'suggestions/suggestion_list.html', {"methods": methods})


@login_required(login_url="/accounts/login/")
def suggestion_detail(request, slug):
    suggestion = Method.objects.get(slug=slug)
    return render(request, "suggestions/suggestion_detail.html", {"suggestion": suggestion})
