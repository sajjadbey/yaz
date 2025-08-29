from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search_words, name="search_words"),
    path('all', views.all_words, name='all_words'),
    path('<str:word>', views.single_word, name='single_word'),
    path('en/<str:translation>', views.search_en, name='search_en'),
]
