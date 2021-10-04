from django.db.models import Q
from apps.core.models import Student, Teacher
from apps.core.choices import Gender

UNDER_AGE = 18

# ModelName.ManagerObj.display_all_records()
students = Student.objects.all()


print(students)

print(students.query)

"""
SELECT "core_student"."id", "core_student"."firstname", "core_student"."name_ar", 
"core_student"."name_en", "core_student"."surname", "core_student"."age", "core_student"."classroom",
"core_student"."teacher", "core_student"."gender"
FROM "core_student"
"""

####################################################################################################


print("#" * 100)
males = Student.objects.get_males()

print(males)

print("#" * 100)


####################################################################################################


females = Student.objects.get_females()

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
qs = Student.objects.get_males().filter(age__lte=25)

print(qs)


print("#" * 100)

# #######################################  AND ###########################################################
qs = Student.objects.get_males().filter(age__lte=25).filter(classroom=2)

print(qs)


print("#" * 100)


# #######################################  Combine queries ###########################################################
under_age_females = Student.objects.get_under_age_females()

print(under_age_females)

under_age_males = Student.objects.get_under_age_males()

print(under_age_males)

print("#" * 100)

# ####################################### exclude with exclude method and ~ operator ###########################

adults = Student.objects.exclude(age__lte=18)

print(adults)

adults = Student.objects.filter(age__gt=18)

print(adults)

adults = Student.objects.filter(~Q(age__lte=18))

print(adults)

print("#" * 100)


# ####################################### gte, gt, lte, lt ###########################

under_20 = Student.objects.filter(age__lt=20)

print(under_20)

ages_20_or_older = Student.objects.filter(age__gte=20)

print(ages_20_or_older)

between10_20 = Student.objects.filter(age__range=[10, 20])

print(between10_20)
not_older_20 = Student.objects.exclude(
    age__gt=20
)  # = age__lt=20: remove objs greater that 20
print(not_older_20)
not_older_20 = Student.objects.filter(age__lt=20)  # get objs less than 20

print(not_older_20)

not_older_20 = Student.objects.filter(
    ~Q(age__gte=20)
)  # remove objs greater that equal 20{

print(not_older_20)

print("#" * 100)


# ####################################### only : select individuals fields ###########################

qs = Student.objects.filter(gender__exact=Gender.FEMALE).only("firstname", "age")

print(qs)

for student in qs:
    print(student.firstname, student.age, student.salary)

print("#" * 100)


# ####################################### raw: using sql raw ###########################

# using to perform another action like index, limit, ....

students = Student.objects.raw("SELECT * FROM core_student WHERE id = 7;")

for student in students:
    print(student)

print("#" * 100)


# ####################################### reverse the ordering of the queryset ###########################

# reverse works if the ordered  = True
males = Student.objects.get_males().order_by("id")

print(males)
males = males.reverse()
print(males)
# from apps.core.shell.student import *
