from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request) -> HttpResponse:
    # return HttpResponse("Hello World") # Simply return text
    return render(request, "hello.html", {'name':"Dominik"})

def say_hello_noname(request) -> HttpResponse:
    # return HttpResponse("Hello World") # Simply return text
    return render(request, "hello.html")