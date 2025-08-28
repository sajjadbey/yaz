from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path("convert/", views.convert_page, name="convert_page"),
    path('api/dict/', include('dict.urls')),
    path('api/utils/', include('yaz_utils.urls')),  # API base
]
