# views.py
from django.shortcuts import render

def convert_page(request):
    return render(request, "convert.html")

def dictionary_page(request):
    return render(request, 'dictionary.html')
