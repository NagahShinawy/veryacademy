from apps.core.models import Teacher

# ###############  Custom Query with manager and models.Manager.from_queryset ###########################

max_salary_for_primary = Teacher.objects.max_salary_for_primary()

print(max_salary_for_primary)


# from apps.core.shell.teacher import *
