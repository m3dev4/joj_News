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
