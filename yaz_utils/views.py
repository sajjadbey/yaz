from django.shortcuts import render
from django.http import JsonResponse
from .utils import OldTurkicConverter  # your converter function

# List of common bot user agents
BOT_USER_AGENTS = [
    "telegram", "instagram", "facebook", "twitter", "whatsapp", "linkedin", "discord"
]

def convert_view(request):
    text = request.GET.get("text", "").strip()
    converted = OldTurkicConverter().convert(text) if text else ""

    user_agent = request.META.get("HTTP_USER_AGENT", "").lower()
    is_bot = any(bot in user_agent for bot in BOT_USER_AGENTS)

    if is_bot:
        # Serve HTML with Open Graph meta
        return render(request, "convert_preview.html", {
            "text": text,
            "converted": converted,
            "url": request.build_absolute_uri(),
        })
    else:
        # Serve normal JSON
        return JsonResponse({"text": text, "converted": converted})
