from django.urls import path
from apps.core.views import students_list, students_list_, students_list_not_s

app_name = "student"

urlpatterns = [
    path("", students_list, name="students_list"),
    path("students/", students_list_, name="students_list_"),
    path("students_not/", students_list_not_s, name="students_list_not_s"),
]
