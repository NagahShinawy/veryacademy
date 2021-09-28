from apps.core.models import Teacher

# ###############  Custom Query with manager and models.Manager.from_queryset ###########################

max_salary_for_primary = Teacher.objects.get_max_salary_for_primary()

print("PRIMARY")
print(max_salary_for_primary)

print("#" * 100)

# #######################################  ###########################################################
max_salary_for_mid = Teacher.objects.get_max_salary_for_mid()

print("MID")
print(max_salary_for_mid)


print("#" * 100)

# #######################################  ###########################################################
max_salary_for_expert = Teacher.objects.get_max_salary_for_expert()


print("EXPERT")
print(max_salary_for_expert)


print("#" * 100)

# #######################################  ###########################################################


max_salary = Teacher.objects.get_max_salary()

print("ALL")

print(max_salary)

print("#" * 100)

# #######################################  ###########################################################

print("Max Age")

max_age = Teacher.objects.max_age()

print(max_age)

print("#" * 100)

# #######################################  ###########################################################
primary = Teacher.objects.primary().order_by("-salary")
mid = Teacher.objects.mid_level().order_by("-salary")
expert = Teacher.objects.expert().order_by("-salary")


print("PRIMARY")
print(primary)

print("MID")
print(mid)

print("Expert")
print(expert)
# from apps.core.shell.teacher import *
