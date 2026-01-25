from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import SectionProjects, Skills


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    section_projects = SectionProjects.objects.all().order_by("-id")
    info_skills = Skills.objects.all().order_by("id")

    return render(
        request,
        "jhones/pages/home.html",
        context={
            "section_projects": section_projects,
            "info_skills": info_skills,
        },
    )


def project(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "jhones/pages/project.html",
    )
