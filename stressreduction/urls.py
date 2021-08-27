from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('suggestions/', include('suggestions.urls')),
    path('about/', views.about, name="about"),
    path('', views.homepage, name="home"),
    path('index', views.homepage2, name="home2"),
    path('slevel', views.stress_level, name="s_level"),
    path('test', views.test, name="test")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
