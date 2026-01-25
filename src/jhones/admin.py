from django.contrib import admin

from .models import MyServices, SectionProjects, Skills, Social


# Register your models here.
@admin.register(SectionProjects)
class sectionProjectsAdmin(admin.ModelAdmin): ...


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin): ...


@admin.register(MyServices)
class MyServicesAdmin(admin.ModelAdmin): ...


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin): ...
