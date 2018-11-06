from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def test(request):
    return HttpResponse('我是一段文字')


def index(request):
    return render(request, 'zhihu/index.html')


def heard(request):
    return render(request, 'zhihu/heard.html')


def hbf(request):
    return render(request, 'zhihu/heard_body_floot.html')


def ext(request):
    return render(request, 'zhihu/ext.html')


# 小括号传参


def a1(request, y, m, s):
    # y=redirect()
    abc = y + '年' + m + '月' + s + '月'
    return HttpResponse(abc)


# 分组命名匹配（形参位置不固定，自需要名字对应就行）


def a2(request, y, m, s, name):
    zxc = y + '年' + m + '月' + s + '月'
    return HttpResponse(zxc + name)


def a3(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    return HttpResponse('name=' + name + 'age=' + age)


# 加载登录页面


def login(request):
    return render(request, 'zhihu/login.html')


# 加载注册


def res(request):
    return render(request, 'zhihu/res.html')


# 验证登录


def do_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username + "  " + password)
    if username == 'admin' and password == '123456':
        return render(request, 'zhihu/index.html')
    else:
        return render(request, 'zhihu/login.html', {
            'username': username,
            'password': password
        })
