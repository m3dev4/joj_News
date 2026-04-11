from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("register/", views.register, name="register"),
    path("articles/", views.list_articles, name="articles"),
    path("articles/<int:id>/", views.detail_article, name="detailArticle"),
    path("articles/<int:pk>/ajouter-commentaire/", views.ajout_commentaire, name="ajout-commentaire"),
    path("articles/<int:pk>/commenter/", views.UpdateCommentaire.as_view(), name="updateCommentaire"),
    path("articles/<int:pk>", views.supprimer_commentaire, name="supprimerCommentaire"),
    
]

