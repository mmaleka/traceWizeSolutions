# tracewizesolutions/urls.py
from django.contrib import admin
from django.urls import path, include  # include is important
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', include('blog.urls')),  # Include blog app at root path
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)