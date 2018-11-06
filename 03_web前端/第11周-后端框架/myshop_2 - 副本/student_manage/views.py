from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from student_manage.models import Student, Manage
import random
import json


def demo(request):
    return render(request, 'student_manage/../templates/shop/demo.html')


# 显示主页
def index(request):
    return render(request, 'student_manage/index.html')


# 显示添加页面
def add(request):
    return render(request, 'student_manage/add.html')


# 执行添加操作
def do_add(request):
    name = request.POST.get('name')
    num = random.randint(100009, 999999)
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    zhuanye = request.POST.get('zhuanye')
    clas = request.POST.get('clas')

    while Student.objects.filter(num=num):
        num = random.randint(100009, 999999)
    Student.objects.create(name=name, num=num, sex=sex, age=age, zhuanye=zhuanye, clas=clas)
    return redirect(reverse('add'))


# 显示学生信息页面
def show(request):
    con = {
        'lists': Student.objects.all(),
    }
    return render(request, 'student_manage/show.html', con)


# 显示注册页面
def res(request):
    return render(request, 'student_manage/res.html')


# 执行注册操作

def do_res(resquest):
    name = resquest.POST.get('name')
    pswd = resquest.POST.get('pswd')
    Manage.objects.create(name=name, pswd=pswd)
    return redirect(reverse('login'))


# 执行登录操作
def do_login(request):
    name = request.POST.get('name')
    pswd = request.POST.get('pswd')
    print('前端密码' + pswd)
    try:
        # 查找到该用户的对象
        obj = Manage.objects.get(name=name)  # 没错误说明查到了该对象
        if obj.pswd == pswd:
            request.session['username'] = name  # 将该对象的密码与前台密码比较
            print('数据库密码' + obj.pswd)
            con = {
                'username': name
            }
            return redirect(reverse('index'), con)
        else:
            return HttpResponse(
                "<script>window.location.href='" + reverse('login') + "';alert('用户名或密码错误')</script>")
    except:
        return HttpResponse(
            "<script>window.location.href='" + reverse('login') + "';alert('用户名或密码错误')</script>")

    return redirect(reverse('index'))


# 显示登录页面
def login(request):
    return render(request, 'student_manage/login.html')


# 注销
def logout(request):
    del request.session['username']
    # return HttpResponse(request.session['username'])
    return redirect(reverse('index'))


# 阅读
def yuedu(request):
    return render(request, 'student_manage/yuedu.html')


# 娱乐
def yule(request):
    print(11111111111111)
    return render(request, 'student_manage/yule.html')


# 检测
def jiance(request):

    return render(request, 'student_manage/login_jiance.html')


# 删除
def dell(request, id):
    print(id+'--------')
    res = Student.objects.filter(num=id).delete()
    if res:
        return HttpResponse("111111111111")
    else:
        return HttpResponse("删除失败")


# 执行跟新操作
def update(request):
    num = request.POST.get('num')
    name = request.POST.get('name')
    # sex = request.POST.get("sex")
    age = request.POST.get('age')
    zhuanye = request.POST.get('zhuanye')
    clas = request.POST.get('clas')
    Student.objects.filter(num=num).update(name=name, age=age, zhuanye=zhuanye, clas=clas)
    con = {
        'status': 'success'
    }
    return HttpResponse(json.dumps(con), content_type='application/json')


def xiugai(request):
    num = request.POST.get('num')
    obj = Student.objects.get(num=num)
    name = obj.name
    sex = obj.sex
    age = obj.age
    zhuanye = obj.zhuanye
    clas = obj.clas

    con = {
        "name": name,
        "sex": sex,
        "age": age,
        "zhuanye": zhuanye,
        "clas": clas,
    }
    return HttpResponse(json.dumps(con), content_type='application/json')
