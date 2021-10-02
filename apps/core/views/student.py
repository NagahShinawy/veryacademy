from django.db import connection
from django.db.models import Q
from django.shortcuts import render
from apps.core.models import Student
from apps.core.choices import Gender


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


def students_and(request):
    students = Student.objects.filter(Q(gender__exact=Gender.FEMALE) & Q(age__lt=30))
    students_2 = Student.objects.filter(Q(id__gt=3) & Q(gender__exact=Gender.FEMALE) & Q(firstname__iendswith="a"))
    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students, "stds": students_2},
    )


def under_ages(request):
    # check managers to filter ages
    females_underage = Student.objects.filter(Q(age__gt=18) & Q(gender__exact=Gender.FEMALE))
    males_underage = Student.objects.filter(Q(age__gt=18) & Q(gender__exact=Gender.MALE))
    return render(
        request=request,
        template_name="students/home.html",
        context={"students": females_underage, "males_underage": males_underage},
    )
