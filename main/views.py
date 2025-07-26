from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    return render(request, "main/index.html")


def about(request) -> HttpResponse:
    return HttpResponse('About')