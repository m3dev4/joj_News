from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Articles
from .forms import CommentaireForm


def accueil(request):
    return render(request, "accueil.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accueil")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

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