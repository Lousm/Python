from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test(request):
    return HttpResponse('我是一段文字')

def index(request):
    return render(request, 'hello/index.html')
