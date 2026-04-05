from django.contrib import admin
from .models import Articles

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "contenu", "date")
    search_fields = ("titre", "contenu")
    ordering = ("-date",)

admin.site.register(Articles, ArticleAdmin)

