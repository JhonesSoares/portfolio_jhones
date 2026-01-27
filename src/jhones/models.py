from django.db import models

from utils.image_size import imageSize


# Create your models here.
class SectionProjects(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    cover = models.ImageField(
        upload_to="jhones/covers/%Y/%m/%d/", blank=True, default=""
    )
    image = imageSize()
    text = models.TextField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cover:
            self.image.resize_image(self.cover, 800)

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=50)
    cover = models.ImageField(
        upload_to="jhones/covers/%Y/%m/%d/", blank=True, default=""
    )
    image = imageSize()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cover:
            self.image.resize_image(self.cover, 100)

    def __str__(self):
        return self.name


class MyServices(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=265)

    def __str__(self):
        return self.title


class Social(models.Model):
    name = models.CharField(max_length=65)
    icon = models.CharField(max_length=100)
    url = models.CharField(max_length=265)

    def __str__(self):
        return self.name
