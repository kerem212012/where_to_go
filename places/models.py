from django.db import models


class Image(models.Model):
    title = models.CharField(verbose_name='Имя', max_length=40)
    image = models.ImageField(verbose_name="картинка")

    def __str__(self):
      return f"{self.title}"

class Place(models.Model):
  title = models.CharField(verbose_name='Имя', max_length=40)
  image = models.ManyToManyField(
    Image,
    related_name="images",
    verbose_name="картинки",
  )
  description_short = models.TextField(verbose_name="краткое описание", blank=True)
  description_long = models.TextField(verbose_name="длинное описание", blank=True)
  lat = models.FloatField(verbose_name="широта")
  lng = models.FloatField(verbose_name="долгота")

  def __str__(self):
    return f"{self.title}"
