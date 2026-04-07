from django.shortcuts import get_object_or_404
from article.models import Articles, Categories , Commentaires
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login
from forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .forms import CommentaireForm


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


def detail_article(request, id):
    article = get_object_or_404(Articles, id=id)
    return render(request, "detailArticle.html", {"article": article})

class ArticleListView(ListView):
    model = Articles
    template_name = 'articles/liste.html'
    context_object_name = 'articles'
    ordering = ['-date']

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'articles/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentaires'] = self.object.commentaires.all()
        context['form'] = CommentaireForm()
        return context

@login_required
def ajout_commentaire(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.auteur = request.user
            commentaire.save()
    return redirect('article-detail', pk=pk)

@login_required
def supprimer_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaires, pk=pk)
    if request.user == commentaire.auteur:
        commentaire.delete()
    return redirect('article-detail', pk=commentaire.article.pk)

@login_required
def modifier_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaires, pk=pk)

    if request.user != commentaire.auteur:
        return redirect('article-detail', pk=commentaire.article.pk)

    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('article-detail', pk=commentaire.article.pk)
    else:
        form = CommentaireForm(instance=commentaire)

    return render(request, 'modifier_commentaire.html', {'form': form})