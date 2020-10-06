from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GallerySerializers
from .models import Gallery


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List gallery sections': '/gallery-sections/',
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
