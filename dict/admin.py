from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('latin', 'arabic_script', 'old_turkic', 'translation_en', 'translation_fa')
    search_fields = ('latin', 'arabic_script', 'old_turkic')
