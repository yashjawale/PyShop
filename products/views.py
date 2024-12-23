from django.shortcuts import render
from django.http import HttpResponse

# /products -> index
def index(request):
    return HttpResponse('Hello World')
