import random
from .models import ContactUs

STATUS = ("single", "married")

objs = ContactUs.objects.all()

for obj in objs:
    obj.status = random.choice(STATUS)
    obj.save()
