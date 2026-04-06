from article.models import Articles, Categorie
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login
from .form import CustomUserCreationForm


def accueil(request):
    return render(request, "accueil.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accueil")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def list_articles(request):
    articles = Articles.objects.all()
    categories = Categorie.objects.all()
    return render(
        request, "articles.html", {"articles": articles, "categories": categories}
    )
