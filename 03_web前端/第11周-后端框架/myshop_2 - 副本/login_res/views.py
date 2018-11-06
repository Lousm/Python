from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from login_res.models import User
import pymysql
import hashlib

md5 = hashlib.md5()
db = pymysql.connect('localhost', 'root', '123456', 'mysql')
cur = db.cursor()


# 显示注册页面
def res(request):
    try :
        del request.session['error']
    except:
        return render(request, 'login_res/res.html')
    return render(request, 'login_res/res.html')


# 注册操作
def do_res(request):
    name = request.POST.get('username')

    # md5.update(request.POST.get('pswd').encode('utf-8'))
    # pswd=md5.hexdigest()
    if not User.objects.filter(name=name):
        pswd = request.POST.get('pswd')
        phone = request.POST.get('phone')
        User.objects.create(name=name, pswd=pswd, phone=phone)
        return redirect(reverse('login'))  # 注册成功，重定向到登录页面
    else:
        request.session['error'] = '用户名已存在'
        con={
            'pswd':request.POST.get('pswd'),
            'phone':request.POST.get('phone'),
        }
        return render(request,'login_res/res.html',con)


# 显示登录页面
def login(request):
    return render(request, 'login_res/login.html')


# 登录操作
def do_login(request):
    username = request.POST.get('username')
    # md5.update(request.POST.get('pswd').encode('utf-8'))
    # pswd = md5.hexdigest()
    pswd = request.POST.get('pswd')
    print('前端密码' + pswd)
    try:
        # 查找到该用户的对象
        obj = User.objects.get(name=username)  # 没错误说明查到了该对象
        if obj.pswd == pswd:
            request.session['username'] = username  # 将该对象的密码与前台密码比较
            print('数据库密码' + obj.pswd)
            con = {
                'username': username
            }
            return redirect(reverse('index'), con)
        else:
            return render(request, 'login_res/login_error.html')
    except:
        return render(request, 'login_res/login_error.html')


# 显示登录错误页面
def login_error(request):
    return render(request, 'login_res/login_error.html')


def index(request):
    return render(request, 'login_res/index.html')


# 注销
def logout(request):
    del request.session['username']
    # return HttpResponse(request.session['username'])
    return redirect(reverse('index'))


# 显示个人信息
def xinxi(request):
    username = request.session['username']
    print(username)
    lists = User.objects.get(name=username)
    print(lists)
    con = {
        "list": lists
    }
    try :
        del request.session['suss']
    except:
        return render(request, 'login_res/xinxi.html', con)
    return render(request, 'login_res/xinxi.html', con)


# 保存个人信息
def do_xinxi(request):
    username = request.POST.get('username')
    sex = request.POST.get('sex')
    print('性别'+sex)
    age = request.POST.get('age')
    phone = request.POST.get('phone')
    eml = request.POST.get('eml')
    jianjie = request.POST.get('jianjie')
    lists = User.objects.get(name=username)
    res = User.objects.filter(name=username).update(sex=sex, age=age, phone=phone, eml=eml, jianjie=jianjie)
    if res:
        con = {
            'suss': '修改成功',
            "list": lists
        }
        request.session['suss'] = '修改成功'
        return redirect(reverse('xinxi'), con)
        # return render(request,'login_res/xinxi.html', con)
    else:
        return HttpResponse('修改失败')


# 显示欢迎小标题
def huanying(requset):
    return render(requset, 'login_res/huanying_biaoti.html')
