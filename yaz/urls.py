from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dict/', include('dict.urls')),
    path('api/utils/', include('yaz_utils.urls')),  # API base
]
