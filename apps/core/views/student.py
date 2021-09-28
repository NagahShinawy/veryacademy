from django.db import connection
from django.shortcuts import render
from apps.core.models import Student


def students_list(request):
    students = Student.objects.all().order_by("id")
    print(students.query)  # get SQL query
    # print(connection.queries)

    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students},
    )
