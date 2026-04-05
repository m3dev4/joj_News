from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout


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

def login_view(request):
    return render(request, "login.html")

def logout_view(request):
    return render(request, "logout.html")   

