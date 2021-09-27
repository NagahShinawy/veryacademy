from django.db.models import Q
from apps.core.models import Student

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


# from apps.core.shell.student import *
