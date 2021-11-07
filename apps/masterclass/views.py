from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, Http404, HttpResponse
from django.template import loader
from .models import Book


def books(request):
    template = loader.get_template("masterclass/books.html")
    return HttpResponse(template.render(context={"books": Book.objects.all()}, request=request))
    # return render(request, books_template, {"books": Book.objects.all()})


def book_details(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    
    except ObjectDoesNotExist:
        raise Http404
    return render(request, "masterclass/book.html", {"book": book})