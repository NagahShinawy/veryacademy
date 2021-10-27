from .models import Note


note_with_no_users = Note.objects.filter(owner__isnull=True)


note_with_no_users.delete()