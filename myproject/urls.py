from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('news.urls')),
    path('', include('catagory.urls')),
    path('', include('subcatagory.urls')),
    path('', include('contactform.urls')),
    path('', include('usermanager.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)