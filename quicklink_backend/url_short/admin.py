from django.contrib import admin
from .models import URLModel

@admin.register(URLModel)
class URLAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'created_at')