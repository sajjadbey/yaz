from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import OldTurkicConverter

@api_view(['GET'])
def latin_to_oldturkic(request):
    """
    Convert Azerbaijani Latin text to Old Turkic runes.
    Usage: /api/dict/convert?text=salam
    """
    text = request.GET.get("text", "")
    if not text:
        return Response({"error": "No text provided"}, status=400)

    converted = OldTurkicConverter.convert(text)
    return Response({
        "latin": text,
        "old_turkic": converted
    })
