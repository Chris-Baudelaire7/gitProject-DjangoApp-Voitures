from django.shortcuts import render
from .models import Teams


def home(request):
    teams = Teams.objects.all()
    context = {"teams": teams}
    return render(request, "pages/home.html", context)


def about(request):
    teams = Teams.objects.all()
    context = {"teams": teams}
    return render(request, "pages/about.html", context)


def cars(request):
    return render(request, "pages/cars.html")


def services(request):
    return render(request, "pages/services.html")


def contact(request):
    return render(request, "pages/contact.html")