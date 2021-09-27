from django.urls import path
from apps.core.views import students_list

app_name = "student"

urlpatterns = [path("", students_list, name="students_list")]
