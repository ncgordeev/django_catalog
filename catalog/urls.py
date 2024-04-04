from django.urls import path

from catalog.views import rendering_index, rendering_contacts

urlpatterns = [
    path('', rendering_index),
    path('contacts/', rendering_contacts),
]
