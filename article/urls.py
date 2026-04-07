from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
]

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/commenter/', views.ajout_commentaire, name='ajout-commentaire'),
]