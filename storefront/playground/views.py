from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # return HttpResponse('hello world')
    return render(request,'index.html',{'name':'ihsaan'})
