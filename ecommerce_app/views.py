from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def res(request):
    return HttpResponse("Hi there")
