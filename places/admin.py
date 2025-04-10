from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image

IMAGE_HEIGHT = 200
IMAGE_WIDTH = 200
class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ("show_preview",)

    def show_preview(self,image):
        return mark_safe(f"<img src='{image.image.url}' width='{IMAGE_WIDTH}' height= '{IMAGE_HEIGHT}'>")

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
