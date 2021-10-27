from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Note


@receiver(pre_save, sender=Note)
def update_note_with_creator(sender, instance, **kwargs):
    pass
