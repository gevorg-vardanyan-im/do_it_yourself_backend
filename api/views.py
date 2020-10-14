from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import \
    GallerySerializers, \
    GalleryFolderSerializers, \
    GalleryFolderImageSerializers
from .models import Gallery, GalleryFolder, GalleryFolderImage


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List gallery sections': '/gallery-sections/',
        'List gallery section folders': '/gallery-section-folders/<int:pk>',
        'List gallery section folder images':
            'gallery-section-folders/<int:section_id>/<int:folder_id>/images',

        'Gallery section\'s detail': '/gallery-section-detail/<str:pk/>',
        'Create gallery section': '/gallery-section-create/',
        'Update gallery section': '/gallery-section-update/<str:pk>/',
        'Delete gallery section': '/gallery-section-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def gallery_sections(request):
    sections = Gallery.objects.all()
    serializer = GallerySerializers(sections, many=True,
                                    context={"request": request})
    return Response(serializer.data)


@api_view(['GET'])
def gallery_section_folders(request, section_id):
    section = get_object_or_404(Gallery, id=section_id)
    # print("===================section =", section)
    # print("===================section =", section.id)
    # folders = GalleryFolder.objects.filter(gallery_id=section.id)
    folders = GalleryFolder.objects.filter(gallery=section)
    serializer = GalleryFolderSerializers(folders, many=True,
                                          context={"request": request})
    return Response(serializer.data)


@api_view(['GET'])
def gallery_section_folder_images(request, folder_id):
    images = GalleryFolderImage.objects.filter(folder_id=folder_id)
    print("\n========== folder images =>", images)

    serializer = GalleryFolderImageSerializers(images, many=True,
                                               context={"request": request})

    print("\n========== folder images =>", serializer.data)
    return Response(serializer.data)
