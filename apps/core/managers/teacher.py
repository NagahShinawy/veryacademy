from django.db import models

from apps.core.choices import ExperienceLevel


class TeacherQS(models.QuerySet):
    def primary(self):
        return self.filter(level=ExperienceLevel.PRIMARY)

    def mid_level(self):
        return self.filter(level=ExperienceLevel.MIDLEVEL)

    def expert(self):
        return self.filter(level=ExperienceLevel.EXPERT)


class SalaryManagerMixin(models.Manager.from_queryset(TeacherQS)):
    def get_records(self, max_salary):
        return self.filter(salary=max_salary)

    def get_max_salary(self):
        max_salary = self.aggregate(models.Max("salary"))["salary__max"]
        return self.get_records(max_salary)

    def get_max_salary_for_primary(self):
        max_salary = self.primary().aggregate(models.Max("salary"))[
            "salary__max"
        ]  # {'salary__max': Decimal('5000.00')}
        return self.get_records(max_salary)

    def get_max_salary_for_mid(self):
        max_salary = self.mid_level().aggregate(models.Max("salary"))["salary__max"]
        return self.get_records(max_salary)

    def get_max_salary_for_expert(self):
        max_salary = self.expert().aggregate(models.Max("salary"))["salary__max"]
        return self.get_records(max_salary)


class AgeManagerMixin(models.Manager):
    def min_age(self):
        return self.order_by("-dob").first()

    def max_age(self):
        return self.order_by("-dob").last()


class TeacherManager(SalaryManagerMixin, AgeManagerMixin):
    def find_by_name(self, query):
        return self.filter(firstname__icontains=query)

    def find_by_surname(self, query):
        return self.filter(surname__icontains=query)
