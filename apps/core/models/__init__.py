from .book import Book
from .student import Student, Teacher
from .quiz import Quizzes, Category
from .utils import dictfetchall, namedtuplefetchall

__all__ = ["Student", "Teacher", "dictfetchall", "namedtuplefetchall", "Book", "Quizzes", "Category"]
