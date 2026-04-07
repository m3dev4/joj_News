from django.contrib import admin
from .models import Articles
from .models import Categories
from .models import Commentaires

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "contenu", "date")
    list_filter = ("date",)
    search_fields = ("titre", "contenu")
    ordering = ("-date",)

admin.site.register(Articles, ArticleAdmin)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    search_fields = ("nom",)
admin.site.register(Categories, CategorieAdmin)

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ("contenu", "date", "article", "auteur")
    list_filter = ("date",)
    search_fields = ("contenu",)
    ordering = ("-date",)
admin.site.register(Commentaires, CommentaireAdmin)
