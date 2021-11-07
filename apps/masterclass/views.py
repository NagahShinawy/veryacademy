from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, Http404
from .models import Book


def books(request):
    return render(request, "masterclass/books.html", {"books": Book.objects.all()})


def book_details(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    
    except ObjectDoesNotExist:
        raise Http404
    return render(request, "masterclass/book.html", {"book": book})