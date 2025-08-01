from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    context = {'title': "Home - главная",
               'content': 'Магазин мебели HOME'
               }
    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    context = {'title': "Home - О нас",
               'content': 'О нас',
               'text_on_page': "Текст о магазине"
               }
    return render(request, "main/about.html", context)