from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import rendering_index, rendering_contacts, rendering_product

urlpatterns = [
                  path('', rendering_index),
                  path('contacts/', rendering_contacts),
                  path('product/<int:pk>', rendering_product)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
