from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<center><h1>Hello {} de {} anos</h1></center>'.format(nome, idade))
