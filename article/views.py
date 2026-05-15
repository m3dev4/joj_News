from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from article.models import Articles, Categories, Commentaires
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CommentaireForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import ollama


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
    categories = Categories.objects.all()
    return render(
        request, "articles.html", {"articles": articles, "categories": categories}
    )


def categorie_article_by_categortie(request, id):
    categorie = Categories.objects.get(id=id)
    articles = Articles.objects.filter(categorie=categorie)
    categories = Categories.objects.all()

    return render(
        request, "articles.html", {"articles": articles, "categories": categories}
    )


def detail_article(request, id):
    article = get_object_or_404(Articles, id=id)
    form = CommentaireForm()
    commentaires = Commentaires.objects.filter(article=article).order_by("-date")
    return render(
        request,
        "detailArticle.html",
        {"article": article, "form": form, "commentaires": commentaires},
    )


@login_required
def ajout_commentaire(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.auteur = request.user
            commentaire.save()
    return redirect("detailArticle", id=pk)


@login_required
def supprimer_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaires, pk=pk)
    if request.user == commentaire.auteur:
        commentaire.delete()
    return redirect("detailArticle", id=commentaire.article.pk)


class UpdateCommentaire(LoginRequiredMixin, UpdateView):
    model = Commentaires
    fields = ["contenu"]
    success_url = "detailArticle.html"

    def get_success_url(self):
        return reverse_lazy("detailArticle", kwargs={"id": self.object.article.pk})


def resume_article(request, id):
    article = get_object_or_404(Articles, id=id)

    try:

        if article.resume:
            resume = article.resume
            return render(
                request, "detailArticle.html", {"article": article, "resume": resume}
            )

        else:
            content_limite = article.contenu[:4000]
            prompt = f"Tu es en experte en rédaction d'article. Résume l'article suivant en quelques mots sans perdre le contexte. tu n'as pas besoin de specialiser les nombres : {content_limite}"
            response = ollama.chat(
            model="mistral", messages=[{"role": "user", "content": prompt}]
            )
            resume = response["message"]["content"]
            article.resume = resume
            article.save()
            return render(
                request, "detailArticle.html", {"article": article, "resume": resume}
            )

    except Exception as e:
        error_message = (
            f"Une erreur s'est produite lors de la génération du résumé : {str(e)}"
        )
        return render(
            request,
            "resumeArticle.html",
            {"article": article, "error_message": error_message},
        )
