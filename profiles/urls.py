from django.urls import path
from profiles import views

urlpatterns = [
    path('audio/convert-audio/', views.conversionView, name='conversion-view'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
