from django.http import HttpResponse

from django.conf import settings
import os


def app(request):
    with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
        return HttpResponse(f.read())
