from . import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import OmahaEventListView, AddListing, about, listing_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about.as_view(), name='about'),
    path('listings/', views.Listings, name='property_listings'),
    path('listings/<int:listing_id>/', listing_detail, name='listing_detail'),
    path('listing_detail/<int:pk>/', listing_detail, name='listing_detail'),
    path('explore/', OmahaEventListView.as_view(), name='omaha_event_list'),
    path('listings/add_listing/', AddListing, name='addlisting'),
   ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
