from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from blog.models import Student


# Create your views here.

# 显示添加页面
def add(request):
    return render(request, 'blog/add.html')


# 添加数据
def do_add(request):
    name = request.POST.get('name')
    xuehao = request.POST.get('xuehao')
    age = request.POST.get('age')
    jianjie = request.POST.get('jianjie')

    Student.objects.create(name=name, xuehao=xuehao, age=age, jianjie=jianjie)
    return redirect(reverse('add'))


inp_id = 1


# 显示数据
def shuju(request):
    global inp_id
    inp_id += 1
    con = {
        'lists': Student.objects.all(),
        'inp_id': [1, 2, 3, 4, 5]
    }
    return render(request, 'blog/shuju.html', con)


# 删除一条数据
def dell(request, id):
    Student.objects.filter(id=id).delete()

    return redirect(reverse('shuju'))


# 数据页input_id自增
def input_id(request):
    global inp_id
    inp_id += 1
    con = {
        'inp_id': [inp_id]
    }
    return render(request, con)


# 显示修改页
def edit(request, id):
    lists = Student.objects.get(id=id)
    con = {
        'list': lists
    }
    return render(request, 'blog/edit.html', con)


# 执行跟新操作
def update(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    xuehao = request.POST.get("xuehao")
    age = request.POST.get('age')
    jianjie = request.POST.get('jianjie')
    res = Student.objects.filter(id=id).update(name=name, xuehao=xuehao, age=age, jianjie=jianjie)
    return redirect(reverse('shuju'))
