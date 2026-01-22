from django.db import models


# Create your models here.
class SectionProjects(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    cover = models.ImageField(
        upload_to="jhones/covers/%Y/%m/%d/", blank=True, default=""
    )

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=50)
    cover = models.ImageField(
        upload_to="jhones/covers/%Y/%m/%d/", blank=True, default=""
    )

    def __str__(self):
        return self.title
