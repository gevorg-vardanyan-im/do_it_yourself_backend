from django.contrib import admin
from .models import Gallery, GalleryFolder

# Register your models here.

# admin.site.register(Gallery)


class GalleryFolderAdmin(admin.StackedInline):
    model = GalleryFolder
    

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryFolderAdmin]

    class Meta:
        model = Gallery


@admin.register(GalleryFolder)
class GalleryFolderAdmin(admin.ModelAdmin):
    pass