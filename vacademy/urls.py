import socket
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls.student", namespace="student")),
    path("", include("apps.core.urls.item", namespace="item")),
    path("books/", include("apps.core.urls.book", namespace="book")),
    path("api/v1/", include("apps.core.urls.quiz", namespace="quiz")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# debug toolbar
if settings.DEBUG and settings.DEBUG_TOOLBAR:
    try:
        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    except ImportError:
        pass
