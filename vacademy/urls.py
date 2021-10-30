import socket
import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static, serve
from .views import index

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("apps.core.urls.student", namespace="student")),
        path("", include("apps.core.urls.item", namespace="item")),
        path("", include("apps.core.urls.server", namespace="server")),
        path("books/", include("apps.core.urls.book", namespace="book")),
        path("api/v1/", include("apps.core.urls.quiz", namespace="quiz")),
        path("api/v1/", include("apps.lne.api.urls", namespace="lns")),
        path("notes/", include("apps.home.urls", namespace="home")),
        path("tryeveything/", index, name="tryeverything"),
        re_path(r"^(?P<path>.*)$", serve, {"document_root": settings.FRONTEND_ROOT}),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

# debug toolbar
if settings.DEBUG and settings.DEBUG_TOOLBAR:
    try:
        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    except ImportError:
        pass
