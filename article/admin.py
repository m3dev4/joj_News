from django.contrib import admin
from .models import Articles, Categorie


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "contenu", "date")
    search_fields = ("titre", "contenu")
    ordering = ("-date",)


admin.site.register(Articles, ArticleAdmin)


class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)
    ordering = ("nom",)


admin.site.register(Categorie, CategorieAdmin)
