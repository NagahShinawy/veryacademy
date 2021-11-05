from django.contrib.auth.models import User
from .models import Book
admin = User.objects.filter(is_superuser=True).first()
books = [
    {"title": "clean code", "creator": admin, "price": 10.4},
    {"title": "python for prof", "creator": admin, "price": 30.9},
    {"title": "flask micro framework", "creator": admin, "price": 20.8},
    {"title": "django for web apps", "creator": admin, "price": 50.9},
    {"title": "js for backend developers", "creator": admin, "price": 60.9},
]

books = [Book(**book) for book in books]


# Insert each of the instances into the database. Do *not* call
# save() on each of the instances, do not send any pre/post_save , signals,

Book.objects.bulk_create(books)

print(Book.objects.all())