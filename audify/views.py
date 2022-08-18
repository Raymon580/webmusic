from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from .forms import RegistrationForm
from .models import User

# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request, "audify/index.html")


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        # Attempt to sign user in
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "audify/login.html", {
                "message": "Invalid username and/or password.",
                "userForm": RegistrationForm()
            })
    else:
        return render(request, "audify/login.html", {
            "userForm": RegistrationForm()
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid() == True:
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Ensure password matches confirmation
            confirmation = request.POST["confirmPassword"]
            if password != confirmation:
                return render(request, "audify/register.html", {
                    "message": "Passwords must match.",
                    "userForm": RegistrationForm()
                })
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "audify/register.html", {
                "message": "Username already taken.",
                "userForm": RegistrationForm()
            })
    else:
        return render(request, "audify/register.html", {
            "userForm": RegistrationForm()
        })
