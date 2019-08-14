from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.photo_list, name="photo_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA, document_root=settings.MEDIA_ROOT)