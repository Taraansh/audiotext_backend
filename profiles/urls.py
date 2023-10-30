from django.urls import path
from .views import conversionView

urlpatterns = [
    path('audio/convert-audio/', conversionView, name='conversion-view' )
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)