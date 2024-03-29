from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book,Publisher,Author
from django.db import connection,models

def main_form(request):
    return render_to_response('main.html')


def search_form(request):
    return render_to_response('search_form.html')


def search_book(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters of book name.')          
        else:
            books = Book.objects.get(title = q)
            authors = books.authors.all()
            publication_date = books.publication_date
            return render_to_response('search_results.html',
                {'books': books,'authors':authors,'publication_date':publication_date, 'query':q})
    
        return render_to_response('search_form.html',{'errors':errors,'q':q})

    elif 'author' in request.GET:
        errors2 = []
        author = request.GET['author']
        if not author:
            errors2.append('Enter a search term.')
        elif len(author) > 20:
            errors2.append('Please enter at most 20 characters of author name.')   
    	else:
            authors = Author.objects.get(first_name = author)
            allbook = authors.book_set.all()
            email = authors.email
	    return render_to_response('search_author_results.html',
                {'allbook':allbook,'email':email,'authors':authors})    
        return render_to_response('search_author.html',{'errors2':errors2,'author':author})


def search_publisher(request):
    return render_to_response('search_publisher_results')


def search_author_form(request):
    return render_to_response('search_author.html')

def search_author(request):
    if 'author' in request.GET:
        author = request.GET['q']
    return render_to_response('search_author_results',{'author':author})
   
 
