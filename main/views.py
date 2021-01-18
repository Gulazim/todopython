from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def first(request):
    return render(request, "page1.html")

def two(request):
    return render(request, "page2.html")

def third(request):
    return render(request, "page3.html")