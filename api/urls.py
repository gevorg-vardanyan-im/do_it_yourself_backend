from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('gallery-sections/', views.gallery_sections, name='gallery-sections'),
    path('gallery-section-folders/<int:section_id>',
         views.gallery_section_folders,
         name='gallery-section-folders'),
]
