from django.db import models
from apps.core.choices import ExperienceLevel


class TeacherQS(models.QuerySet):
    def primary(self):
        return self.filter(level=ExperienceLevel.PRIMARY)

    def mid_level(self):
        return self.filter(level=ExperienceLevel.MIDLEVEL)

    def expert(self):
        return self.filter(level=ExperienceLevel.EXPERT)


class TeacherManager(models.Manager.from_queryset(TeacherQS)):
    def max_salary_for_primary(self):
        max_salary = self.primary().aggregate(models.Max("salary"))[
            "salary__max"
        ]  # {'salary__max': Decimal('5000.00')}
        return self.filter(salary=max_salary)

    def max_salary_for_midlevel(self):
        max_salary = self.mid_level().aggregate(models.Max("salary"))["salary__max"]
        return self.filter(salary=max_salary)

    def max_salary_for_expert(self):
        max_salary = self.expert().aggregate(models.Max("salary"))["salary__max"]
        return self.filter(salary=max_salary)

    def max_salary(self):
        max_salary = self.aggregate(models.Max("salary"))["salary__max"]
        return self.filter(salary=max_salary)
