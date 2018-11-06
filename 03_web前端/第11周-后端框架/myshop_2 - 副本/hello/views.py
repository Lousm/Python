from django.shortcuts import render
from django.http import HttpResponse

#返回文字
def test(request):
    return HttpResponse("我是一段文字")

#返回网页
def index(request):
    return render(request,'hello/index.html')