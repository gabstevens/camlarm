from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('detections/<str:id>', views.detection),
    path('detections', views.detections),
    path('sensors/<str:key>', views.sensor),
    path('sensors', views.sensors),
    path('locations/<str:id>', views.location),
    path('locations', views.locations),
    url(r'^app(?:.*)/?$', views.app, name="app")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
