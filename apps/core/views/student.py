from django.shortcuts import render
from apps.core.models import Student


def students_list(request):
    students = Student.objects.all().order_by("id")

    return render(
        request=request,
        template_name="students/home.html",
        context={"students": students},
    )
