from django.db import connection
from django.db.models import Q
from django.db.models.functions import Lower, Upper, Replace
from django.shortcuts import render
from apps.core.models import Student, Teacher
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
    students_2 = Student.objects.filter(
        Q(id__gt=3) & Q(gender__exact=Gender.FEMALE) & Q(firstname__iendswith="a")
    )
    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students, "stds": students_2},
    )


def under_ages(request):
    # check managers to filter ages
    females_underage = Student.objects.filter(
        Q(age__gt=18) & Q(gender__exact=Gender.FEMALE)
    )
    males_underage = Student.objects.filter(
        Q(age__gt=18) & Q(gender__exact=Gender.MALE)
    )
    print(males_underage)
    print(connection.queries)  # show sql statement and more info about query
    return render(
        request=request,
        template_name="students/home.html",
        context={"students": females_underage, "males_underage": males_underage},
    )


def union(request):
    # get firstname from student Model, and get firstname from teacher Model.
    students = Student.objects.values_list("firstname")
    print(
        students
    )  # <QuerySet [('Nancy',), ('PHP',), ('Smith',), ('Anna',), ('Ella',), ('sara',), ('Adam',), ('John',)]>
    teachers = Teacher.objects.values_list("firstname")
    print(teachers)
    # means get unique firstnames from Student Model and Teacher Model
    firstnames = students.union(
        teachers
    )  # it returns distinct firstnames ignoring case sensitive
    print(students.count())
    print(teachers.count())
    print(firstnames.count())
    print(
        Student.objects.values("firstname")[:3]
    )  # <QuerySet [{'firstname': 'Nancy'}, {'firstname': 'PHP'}, {'firstname': 'Smith'}]>

    print(connection.queries)
    return render(
        request=request,
        template_name="students/home.html",
        context={"firstnames": firstnames},
    )


def salaries(request):
    students_salary = Student.objects.values("salary").order_by("salary").distinct()
    # get all distinct salaries and sort it desc
    # union fields must have the same name and same datatype
    all_salaries = (
        Student.objects.values("salary")
        .union(Teacher.objects.values("salary"))
        .order_by("salary")
    )
    print(all_salaries)

    # UNION types numeric and date cannot be matched
    # qs = Student.objects.values("salary").union(Teacher.objects.values("dob"))
    # print(qs)
    print(connection.queries)
    return render(
        request=request,
        template_name="students/home.html",
        context={"students_salary": students_salary, "all_salaries": all_salaries},
    )


def lower(request):
    # students = Student.objects.values_list(Lower("firstname"))
    students = Student.objects.values_list(Upper("firstname"))
    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students},
    )


def not_query(request):
    # not males = females
    # exclude males means get females
    not_males = Student.objects.exclude(gender=Gender.MALE)
    # means females and adults
    not_males_and_not_underage = Student.objects.exclude(
        (Q(gender=Gender.MALE) | Q(age__lt=18))
    )

    # get adults females
    adult_females = Student.objects.exclude(gender=Gender.MALE).exclude(age__lt=18)

    print(adult_females)
    print(connection.queries)
    return render(
        request=request,
        template_name="students/home.html",
        context={
            "females": not_males,
            "older_females": not_males_and_not_underage,
            "adult_females": adult_females,
        },
    )


def select_individual(request):
    students = Student.objects.values("firstname", "age")
    primary = Student.objects.primary_class().only("firstname", "classroom")
    secondary = Student.objects.secondary_class().only("age", "salary")
    stds = Student.objects.only("firstname")
    print([std.firstname for std in stds])
    print(secondary.query)
    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students, "primary": primary, "secondary": secondary},
    )
