from .book import Author, BasicProfile, Book
from .quiz import Category, Quizzes
from .student import Student, Teacher
from .utils import dictfetchall, namedtuplefetchall

__all__ = [
    "Student",
    "Teacher",
    "dictfetchall",
    "namedtuplefetchall",
    "Book",
    "Quizzes",
    "Category",
    "Author",
    "BasicProfile",
]
