from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def first(request):
    return render(request, "page1.html")

def two(request):
    return render(request, "page2.html")

def third(request):
    return render(request, "page3.html")

def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect (test)

def add_books(request):
    form = request.POST
    title = form["books_title"]
    subtitle = form["books_subtitle"]
    description = form["books_description"]
    price = form["books_price"]
    genre = form["books_genre"]
    author = form["books_author"]
    year = form["books_year"]
    shelf = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    shelf.save()
    return redirect (books)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)