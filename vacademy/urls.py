from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls.student", namespace="student")),
    path("books/", include("apps.core.urls.book", namespace="book")),
    path("api/v1/", include("apps.core.urls.quiz", namespace="quiz")),
]
