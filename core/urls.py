from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # ThirdParty Urls
    path("tinymce/", include("tinymce.urls")),
    path("admin/", admin.site.urls),
    # Apps Urls
    path("", include("blog.urls")),
]

# Add static and media to urlpatterns
urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
