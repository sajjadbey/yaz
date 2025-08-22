from django.urls import path
from .views import convert_view

urlpatterns = [
    path("convert/", convert_view, name="convert"),
]
