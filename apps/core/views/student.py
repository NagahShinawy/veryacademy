from django.db import connection
from django.db.models import Q
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


def students_list_(request):
    # get all qs startswith "S" with 'ignore case sensitive' or qs startswith 'A'
    students = Student.objects.filter(
        firstname__istartswith="S"
    ) | Student.objects.filter(firstname__startswith="A")

    print(students)
    print(
        connection.queries
    )  # show sql statement and more info like LIMIT , time of query execution
    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students},
    )


def students_list_not_s(request):
    # not operator ~. mean get all objs with firstname not sS
    # get all but exclude objs startswith either s or S
    students = Student.objects.filter(~Q(firstname__istartswith="s"))
    exclude_s = Student.objects.exclude(firstname__istartswith="s")

    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students, "students_not_s": exclude_s},
    )
