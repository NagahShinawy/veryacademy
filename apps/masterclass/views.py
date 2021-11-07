from django.shortcuts import render
from .models import Book


def books(request):
    return render(request, "masterclass/books.html", {"books": Book.objects.all()})

