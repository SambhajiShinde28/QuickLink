from django.db import models
import string
import random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

class URLModel(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=500, unique=True, default=generate_short_url)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url
