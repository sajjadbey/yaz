from django.db import models

class Word(models.Model):
    latin = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    arabic_script = models.CharField(max_length=100, blank=True)
    old_turkic = models.CharField(max_length=100, blank=True)
    translation_en = models.TextField(blank=True)
    translation_fa = models.TextField(blank=True)

    def __str__(self):
        return self.latin