from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from .models import Word
from django.db.models import Q
from .serializers import WordSerializer

def all_words(request):
    words = Word.objects.all()
    data = [
        {
            'latin': w.latin,
            'arabic_script': w.arabic_script,
            'old_turkic': w.old_turkic,
            'translation_en': w.translation_en,
            'translation_fa': w.translation_fa
        }
        for w in words
    ]
    return JsonResponse(data, safe=False)

def single_word(request, word):
    # Convert word from URL to lowercase for consistency
    try:
        w = Word.objects.get(latin__iexact=word)  # case-insensitive lookup
    except Word.DoesNotExist:
        return JsonResponse({'error': 'Word not found'}, status=404)
    
    data = {
        'latin': w.latin,
        'arabic_script': w.arabic_script,
        'old_turkic': w.old_turkic,
        'translation_en': w.translation_en,
        'translation_fa': w.translation_fa
    }
    return JsonResponse(data)

def search_en(request, translation):
    # Case-insensitive search for English translation
    words = Word.objects.filter(translation_en__icontains=translation)
    if not words.exists():
        return JsonResponse({'error': 'No words found'}, status=404)

    data = [
        {
            'latin': w.latin,
            'arabic_script': w.arabic_script,
            'old_turkic': w.old_turkic,
            'translation_en': w.translation_en,
            'translation_fa': w.translation_fa
        }
        for w in words
    ]
    return JsonResponse(data, safe=False)

@api_view(["GET"])
def search_words(request):
    query = request.GET.get("q", "")
    if query:
        words = Word.objects.filter(latin__icontains=query)[:20]  # limit results
    else:
        words = Word.objects.none()

    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)

