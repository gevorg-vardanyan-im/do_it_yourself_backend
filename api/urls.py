from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('gallery-sections/', views.gallery_sections, name='gallery-sections'),
]
