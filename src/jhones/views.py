from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import MyServices, SectionProjects, Skills, Social


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    section_projects = SectionProjects.objects.all().order_by("id")
    info_skills = Skills.objects.all().order_by("id")
    services = MyServices.objects.all().order_by("id")
    contacts = Social.objects.all().order_by("id")

    if request.method == "POST":
        name = request.POST.get("contact_name")
        email = request.POST.get("email")
        message = request.POST.get("text_message")

        assunto = f"📩 Nova mensagem do portfólio — {name}"

        corpo = f"""
        Você recebeu uma nova mensagem do seu portfólio:

        Nome: {name}
        Email: {email}

        Mensagem:
        {message}
        """
        email_msg = EmailMessage(
            subject=assunto,
            body=corpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
        )
        email_msg.send()
        messages.success(
            request, "Mensagem enviada com sucesso! Em breve entrarei em contato."
        )

    return render(
        request,
        "jhones/pages/home.html",
        context={
            "section_projects": section_projects,
            "info_skills": info_skills,
            "services": services,
            "contacts": contacts,
        },
    )


def project(request: HttpRequest, id: int) -> HttpResponse:
    section_project = SectionProjects.objects.filter(pk=id).order_by("-id").first()

    return render(
        request,
        "jhones/pages/project.html",
        context={
            "section_project": section_project,
        },
    )
