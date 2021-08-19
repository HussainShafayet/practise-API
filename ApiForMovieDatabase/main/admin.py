from django.contrib import admin
from .models import Movie,Comments

# Register your models here.
admin.site.register(Movie),
admin.site.register(Comments)