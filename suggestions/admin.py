from django.contrib import admin
from .models import Method


class MethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'snippet', 'slug', 'date')


# we need to register our models here to enable django show them in the admin page.
admin.site.register(Method, MethodAdmin)


