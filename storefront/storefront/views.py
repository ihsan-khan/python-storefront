from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.from django.shortcuts import render

def all_blogs(request):
    return HttpResponse("<h1>Welcome to first Project: Home page</h1>")