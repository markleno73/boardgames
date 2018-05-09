from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #return HttpResponse("Hello, World!")
    return render(request, "main/home.html", {'message': 'hi, there!'})