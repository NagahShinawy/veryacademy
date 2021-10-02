from django.db import connection
from django.shortcuts import render
from apps.core.models import Student


def students_list(request):
    students = Student.objects.all().order_by("-id")
    print(students)
    print(students.query)  # get SQL query
    print(
        connection.queries
    )  # more info about query [ run it after query ==> after students = Student.objects.all()]

    # more info about query like LIMIT and time but you have to 'print(students)' to see the result

    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students},
    )
