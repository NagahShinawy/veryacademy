from django.urls import path
from apps.core.views import students_list, students_list_

app_name = "student"

urlpatterns = [
    path("", students_list, name="students_list"),
    path("students/", students_list_, name="students_list_"),
]
