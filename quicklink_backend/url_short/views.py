from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import URLModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect

@csrf_exempt
def create_short_url(request):
    if request.method == "POST":
        data = json.loads(request.body)
        long_url = data.get('long_url')

        if not long_url:
            return JsonResponse({"error": "URL is required"}, status=400)

        url = URLModel.objects.create(long_url=long_url)
        short_url = request.build_absolute_uri(f'/{url.short_url}')

        return JsonResponse({"short_url": short_url}, status=201)
    return JsonResponse({"error": "Invalid request method"}, status=405)



def redirect_to_long_url(request, short_url):
    url = get_object_or_404(URLModel, short_url=short_url)
    return redirect(url.long_url)
