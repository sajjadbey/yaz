from django.urls import path
from .views import latin_to_oldturkic

urlpatterns = [
    path("convert/", latin_to_oldturkic, name="convert_to_old_turkic"),
]
