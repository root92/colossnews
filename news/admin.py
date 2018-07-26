from django.contrib import admin
from .models import Domaine, Article
# Register your models here.
@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'title', 'domaine', 'localisation', 'created', 'updated']

