from django.contrib.auth.models import User
from .models import Book

admin = User.objects.filter(is_superuser=True).first()
books = [
    {"title": "clean code", "creator": admin, "price": 10.4, "has_offer": True},
    {"title": "python for prof", "creator": admin, "price": 30.9, "has_offer": True},
    {"title": "flask micro framework", "creator": admin, "price": 20.8},
    {"title": "django for web apps", "creator": admin, "price": 50.9},
    {
        "title": "js for backend developers",
        "creator": admin,
        "price": 60.9,
        "has_offer": True,
    },
]

books = [Book(**book) for book in books]


# Insert each of the instances into the database. Do *not* call
# save() on each of the instances, do not send any pre/post_save , signals,


def create_all(model, objs):
    model.objects.bulk_create(objs)


def get_offer():
    return Book.objects.filter(has_offer=True).order_by("id")


# create_all(Book, books)

print(Book.objects.all())

print("#" * 100)
print(get_offer())
