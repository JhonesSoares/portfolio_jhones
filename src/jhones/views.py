from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "jhones/pages/home.html",
    )


def project(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "jhones/pages/project.html",
    )
