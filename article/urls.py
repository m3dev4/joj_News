from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("register/", views.register, name="register"),
    path("articles/", views.list_articles, name="articles"),
    
]