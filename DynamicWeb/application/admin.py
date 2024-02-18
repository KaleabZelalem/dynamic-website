from django.contrib import admin
from application.models import Genre, Artist, Movie

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Movie)