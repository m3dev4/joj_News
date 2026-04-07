from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
]

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path('article/<int:pk>/commenter/', views.ajout_commentaire, name='ajout-commentaire'),
    path("register/", views.register, name="register"),
    path("articles/", views.list_articles, name="articles"),
    path("articles/<int:id>/", views.detail_article, name="detailArticle"),
    
]