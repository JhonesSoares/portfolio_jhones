from django.contrib import admin

from .models import SectionProjects, Skills


# Register your models here.
@admin.register(SectionProjects)
class sectionProjectsAdmin(admin.ModelAdmin): ...


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin): ...
