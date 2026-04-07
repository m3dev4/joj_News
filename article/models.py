from django.db import models
from django.conf import settings


class Categories(models.Model):
    nom = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nom


class Articles(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to="articles/", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Commentaires(models.Model):
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenu
