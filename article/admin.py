from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "contenu", "date", "auteur")
    list_filter = ("date", "auteur")
    search_fields = ("titre", "contenu")
    ordering = ("-date",)

admin.site.register(Article, ArticleAdmin)

