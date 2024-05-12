from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import rendering_index, rendering_contacts

urlpatterns = [
                  path('', rendering_index),
                  path('contacts/', rendering_contacts),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
