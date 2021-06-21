from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('realtor/<int:pk>/',Realtor_detail.as_view()),
    path('realtor/',Realtor_view.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)