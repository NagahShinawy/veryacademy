from apps.core.models import Student

students = Student.objects.all()

print(students)

print("#" * 100)
males = Student.objects.get_by_males()

print(males)

print("#" * 100)

females = Student.objects.get_by_females()

print(females)

# from apps.core.shell.student import *