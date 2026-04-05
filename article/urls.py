from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("registrations/register/", views.register, name="register"),
    
]