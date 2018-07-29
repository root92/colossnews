from django.contrib import admin
from .models import Categorie, Article
# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'title', 'domaine', 'localisation', 'created', 'updated']

