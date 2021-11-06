from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse('<center><h1>Hello {} de {} anos</h1></center>'.format(nome, idade))


def soma(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse('<center><h1>A soma de {} + {} = {}</h1></center>'.format(num1, num2, resultado))


def subtracao(request, num1, num2):
    resultado = num1 - num2
    return HttpResponse('<center><h1>A subtração de {} - {} = {}</h1></center>'.format(num1, num2, resultado))


def multiplicacao(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse('<center><h1>A multiplicação de {} x {} = {}</h1></center>'.format(num1, num2, resultado))


def divisao(request, num1, num2):
    resultado = num1 / num2
    return HttpResponse('<center><h1>A divisão de {} / {} = {}</h1></center>'.format(num1, num2, resultado))
