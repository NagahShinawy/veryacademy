from django.db.models import Q
from apps.core.models import Student, Teacher

UNDER_AGE = 18

students = Student.objects.all()

print(students)

####################################################################################################


print("#" * 100)
males = Student.objects.get_by_males()

print(males)

print("#" * 100)


####################################################################################################


females = Student.objects.get_by_females()

print(females)

print("#" * 100)

####################################################################################################

# OR query

qs = Student.objects.filter(
    Q(firstname__istartswith="j") | Q(firstname__istartswith="a")
)

print(qs)

print("#" * 100)

####################################################################################################

qs = Student.objects.filter(age__in=[23, 25])


print(qs)

print("#" * 100)

####################################################################################################


qs = Student.objects.filter(age__lte=30)

print(qs)

print("#" * 100)

####################################################################################################

qs = Student.objects.get_by_age(age=25)


print(qs)

print("#" * 100)

####################################################################################################

under_age = Student.objects.get_under_age()
print(under_age)


print("#" * 100)

# #######################################  AND ###########################################################
qs = Student.objects.get_by_males().filter(age__lte=25)

print(qs)


print("#" * 100)

# #######################################  AND ###########################################################
qs = Student.objects.get_by_males().filter(age__lte=25).filter(classroom=2)

print(qs)


print("#" * 100)

# ###############  Custom Query with manager and models.Manager.from_queryset ###########################

max_salary_for_primary = Teacher.objects.max_salary_for_primary()

print(max_salary_for_primary)

# from apps.core.shell.student import *

