from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^detections$', views.detections, name='detections'),
    url(r'^sensors$', views.sensors, name='sensors'),
    url(r'^app(?:.*)/?$', views.app, name="app")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
