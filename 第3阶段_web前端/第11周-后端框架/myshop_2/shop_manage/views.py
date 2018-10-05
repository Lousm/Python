from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from shop_manage.models import Manage, Power, Role, role_power
from shop.models import Commodity, Classify, Commodity_introduce, Commodity_img, Home_floor, Home_floor_commodity
from django.core.paginator import Paginator
import json, time, os, uuid
from django.conf import settings


def login(request):
    return render(request, 'shop_manage/login.html')


def do_login(request):
    name = request.POST.get('username')
    pswd = request.POST.get('password')
    info = Manage.objects.filter(admin_name=name).first()
    res = Manage.objects.filter(admin_name=name, password=pswd)
    print(1111111111111111111111111111)
    print(info)
    if res:
        request.session['manage_name'] = name
        print(info.id)
        request.session['uid'] = info.id
        print('+++++++++')
        print(info.id)

        con = {
            'data': '',
            'status': 0
        }
        print('----------------------')
        print(info.role.role_power_set.filter())
        # 根据登陆的用户获取对应的权限id
        user_power = []
        for pow in info.role.role_power_set.filter():
            user_power.append(pow.power_id)

        request.session['user_power'] = user_power

        # return HttpResponse('提交')
        return HttpResponse(json.dumps(con), content_type='application/json')
    else:
        con = {
            'data': '用户名或密码错误',
            'status': 1
        }
        return HttpResponse(json.dumps(con), content_type='application/json')


def index(request):



    return render(request, 'shop_manage/index.html')


def goods_add(request):
    obj = Classify.objects.filter().extra({'pId': 'Parentid'}).values('id', 'pId', 'name')
    json_obj = json.dumps(list(obj))

    return render(request, 'shop_manage/goods_add.html', {'json_obj': json_obj})


def goods_list(request):
    obj = Commodity.objects.filter(status=0)
    con = {
        'data': obj
    }

    return render(request, 'shop_manage/goods-list.html', con)
    # return redirect(reverse('goods_list_shop_manage'), con)


def add_tyep(request):
    obj = Classify.objects.filter().extra({'pId': 'Parentid'}).values('id', 'pId', 'name')
    json_obj = json.dumps(list(obj))

    # print(json_obj)
    return render(request, 'shop_manage/add_type.html', {'json_obj': json_obj})


def do_add_tyep(request):
    name = request.POST.get('name')
    parent_id = request.POST.get('parent_id')
    Classify.objects.create(name=name, Parentid=parent_id, add_time=time.time(),
                            add_user_id_id=request.session.get('uid'))
    return redirect(reverse('add_tyep_shop_manage'))


# 修改商品信息
def xiugai(request):
    id = request.POST.get('id')
    obj = Commodity.objects.get(id=id)
    name = obj.name
    jiage = obj.price
    number = obj.number
    addtime = obj.add_time
    adduser = obj.add_adminuser_id.realname

    con = {
        'name': name,
        'jiage': str(jiage),
        'number': number,
        'addtime': addtime,
        'adduser': adduser,
    }
    return HttpResponse(json.dumps(con), content_type='application/json')


# 修改后更新商品信息
def update(request):
    id = request.POST.get('id_s')
    name = request.POST.get('name_')
    jiage = str(request.POST.get('jiage'))
    print(jiage)
    number = request.POST.get('num')
    addtime = 1
    adduser = 1

    Commodity.objects.filter(id=id).update(name=name, price=jiage, number=number, add_time=addtime,
                                           add_adminuser_id_id=adduser)

    con = {'status': 0}

    return HttpResponse(json.dumps(con), content_type='application/json')


def dell(request):
    id = request.POST.get('id')
    Commodity.objects.filter(id=id).update(status=1)
    con = {'status': 0}
    return HttpResponse(json.dumps(con), content_type='application/json')


def do_good_add(request):
    print(request.FILES.getlist('img'))

    # 商品表
    comm = Commodity()
    comm.name = request.POST.get('c_name')
    comm.price = request.POST.get('price')
    comm.number = request.POST.get('number')
    comm.add_time = 1
    comm.add_user_id_id = request.session.get('uid')
    comm.status = 0
    comm.classify_id_id = request.POST.get('types_id')
    tex = request.POST.get('content')
    comm.save()

    # 商品介绍表
    Commodity_introduce.objects.create(commodity_id_id=comm.id, content=tex)

    # 商品图片表
    file_list = request.FILES.getlist('img')  # 上传的文件列表
    for i in file_list:
        hz = i.name.split('.')
        new_name = str(uuid.uuid1()) + '.' + hz[-1]
        new_file = open(os.path.join(settings.MEDIA_ROOT, new_name), 'wb+')  # 创建一个新文件
        for j in i.chunks():
            new_file.write(j)
        new_file.close()

        comm_img = Commodity_img()
        comm_img.path = os.path.join(settings.MEDIA_URL, new_name)
        comm_img.commodity_id_id = comm.id
        comm_img.save()

    return HttpResponse("提交成功")


# 商品
def type_list(request):
    obj = Classify.objects.filter()
    con = {
        'data': obj,
    }
    return render(request, 'shop_manage/type_list.html', con)


# 添加权限
def add_power(request):
    obj = Power.objects.filter().extra({'pId': 'parent_id'}).values('id', 'pId', 'name')
    json_obj = json.dumps(list(obj))

    # print(json_obj)

    return render(request, 'shop_manage/add_power.html', {'json_obj': json_obj})


# 执行添加权限
def do_add_power(request):
    name = request.POST.get('name')
    parent_id = request.POST.get('parent_id')
    control = request.POST.get('control')
    fun = request.POST.get('fun')
    Power.objects.create(name=name, parent_id=parent_id, control=control, fun=fun)
    return redirect(reverse('add_power_shop_manage'))


# 添加角色页面
def add_role(request):
    obj = Power.objects.filter().extra({'pId': 'parent_id'}).values('id', 'pId', 'name')
    json_obj = json.dumps(list(obj))
    return render(request, 'shop_manage/add_role.html', {'json_obj': json_obj})


# 执行添加角色
def do_add_role(request):
    roObj = Role()
    roObj.name = request.POST.get('name')
    roObj.save()

    lis = request.POST.getlist('power_id')
    for pow in lis:
        rpObj = role_power()
        rpObj.power_id = pow
        rpObj.role_id = roObj.id
        rpObj.save()

    return redirect(reverse('add_role_shop_manage'))


# 显示添加楼层商品页面
def add_floor_comm(request):
    floor_obj = Home_floor.objects.filter()
    comm_obj = Commodity.objects.filter()

    con = {
        'floor': floor_obj,
        'comm': comm_obj,
    }
    print('显示添加楼层商品')
    # return redirect(reverse('add_floor_comm_shop_manage'), con)
    return render(request, 'shop_manage/add_floor_comm.html', con)


def do_add_floor_comm(request):
    flo_comm_obj = Home_floor_commodity()
    flo_comm_obj.commodity_id_id = request.POST.get('comm_id')
    flo_comm_obj.floot_id_id = request.POST.get('floor_id')
    flo_comm_obj.paixu = request.POST.get('paixu')
    flo_comm_obj.save()
    return render(request, 'shop_manage/add_floor_comm.html')


# 显示添加楼层
def add_floor(request):
    return render(request, 'shop_manage/add_floor.html')


# 添加楼层
def do_add_floor(request):
    name = request.POST.get('floor_name')
    flie = request.FILES.get('img')

    hz = flie.name.split('.')
    new_name = str(uuid.uuid1()) + '.' + hz[-1]
    new_file = open(os.path.join(settings.MEDIA_ROOT, new_name), 'wb+')  # 创建一个新文件
    for j in flie.chunks():
        new_file.write(j)
    new_file.close()

    flo_obj = Home_floor()
    flo_obj.name = name
    flo_obj.add_user = request.session.get('uid')
    flo_obj.img_path = os.path.join(settings.MEDIA_URL, new_name)
    flo_obj.save()
    return render(request, 'shop_manage/add_floor.html')
