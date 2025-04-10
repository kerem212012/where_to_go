from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Имя', max_length=40)
    description_short = models.TextField(verbose_name="краткое описание", blank=True)
    description_long = HTMLField(verbose_name="длинное описание", blank=True)
    lat = models.FloatField(verbose_name="широта")
    lng = models.FloatField(verbose_name="долгота")

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    image = models.ImageField(verbose_name="картинка")
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name="места",
        related_name="images",
        blank=True,
        null=True

    )
