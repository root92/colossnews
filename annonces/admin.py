from django.contrib import admin
from .models import Entreprise, Annonce, Apply
# Register your models here.
@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ['ent_name', 'adresse_1', 'adresse_2', 'telephone']

class ApplyInline(admin.TabularInline):
    model = Apply

@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ['entreprise', 'job_title', 'description', 'limite_date', 'created', 'updated']
    inlines = [ApplyInline]


    # raw_id_fields = ['art_name']

# @admin.register(Apply)
# class ApplyAdmin(admin.ModelAdmin):
#     list_display = ['annonce', 'first_name', 'middle_name', 'last_name', 'telephone']