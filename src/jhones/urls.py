from django.urls import path

from . import views

app_name = "jhones"

urlpatterns = [
    path("", views.home, name="home"),
    path("projeto/<int:id>/", views.project, name="projeto"),
]
