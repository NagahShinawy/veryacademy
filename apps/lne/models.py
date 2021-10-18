from django.db import models
from apps.core.mixins import BasicInfoMixin


class Member(BasicInfoMixin, models.Model):
    """

    """


class HearingTestData(models.Model):
    label = "Hearing Test"
    left_ear_freq = models.BooleanField(null=True)
    right_ear_freq = models.BooleanField(null=True)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"L [ {self.left_ear_freq} ] - R [ {self.right_ear_freq} ]"
