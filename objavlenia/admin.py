from django.contrib import admin

# Register your models here.
from objavlenia.models import Author, Category, Advertisment

admin.site.register(Author)
admin.site.register( Category)
admin.site.register(Advertisment)