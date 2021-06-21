from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


# routers=DefaultRouter()
# routers.register('listing/',Listing_view)

urlpatterns = [
    path('listing/<int:pk>/',Listing_detail.as_view()),
    # path('listing/<int:pk>/',Listing_detail_1.as_view()),
    # path('listing/',Listing_view),
    path('listing/',Listing_view.as_view()),
    path('listing/search',Listing_search.as_view()),
    # path('listing/searchs',Listing_searchs.as_view()),
    path('listing/home',Listing_home.as_view())

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)