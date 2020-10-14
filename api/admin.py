from django.contrib import admin
from .models import Gallery, GalleryFolder, GalleryFolderImage


# Register your models here.

# admin.site.register(Gallery)

# below are the models-classes

class GalleryFolderAdmin(admin.StackedInline):
    model = GalleryFolder


class GalleryFolderImageAdmin(admin.StackedInline):
    model = GalleryFolderImage


#  below are the models representation

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryFolderAdmin]

    class Meta:
        model = Gallery


@admin.register(GalleryFolder)
class GalleryFolderAdmin(admin.ModelAdmin):
    inlines = [GalleryFolderImageAdmin]

    class Meta:
        model = GalleryFolder


@admin.register(GalleryFolderImage)
class GalleryFolderImageAdmin(admin.ModelAdmin):
    pass
