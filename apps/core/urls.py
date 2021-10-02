from django.urls import path
from apps.core.views import students_list, students_list_, students_list_not_s, students_and, under_ages, union

app_name = "student"

urlpatterns = [
    path("", students_list, name="students_list"),
    path("students/", students_list_, name="students_list_"),
    path("students_not/", students_list_not_s, name="students_list_not_s"),
    path("students_and/", students_and, name="students_and"),
    path("under_ages/", under_ages, name="under_ages"),
    path("union/", union, name="union"),
]
