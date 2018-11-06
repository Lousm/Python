from django.shortcuts import render, reverse, redirect
from shop.models import User
from PIL import Image, ImageDraw, ImageFont
import hashlib, json, random, io, time
from shop import models
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q, F


def res(request):
    return render(request, 'shop/res.html')


def res_1(request):
    return render(request, 'shop/res_1.html')


# 执行注册
def do_res(request):
    md5 = hashlib.md5()
    username = request.POST.get('username')
    # md5.update(bytes(request.POST.get('pswd').encode('utf-8')))
    md5.update(request.POST.get('pswd').encode('utf-8'))
    password = md5.hexdigest()
    User.objects.create(username=username, password=password)
    return redirect(reverse('res_1_shop'))


# 验证用户名是否已经存在
def username1(request):
    username = request.POST.get('username')
    # print(username)
    users = models.User.objects.filter(username=username).first()
    con = {}
    if users == None:
        con['data'] = ''
        con['status'] = 0
    else:
        con['data'] = '用户名已存在'
        con['status'] = 1
    return HttpResponse(json.dumps(con), content_type='application/json')


# 生成验证码
def yzm(request):
    huabu = Image.new('RGB', (135, 55), (222, 222, 222))  # 画布
    huabi = ImageDraw.Draw(huabu)  # 生成画笔
    s_list = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefjhijkmnpqrstuvwxyc23456789'  # 56个
    font = ImageFont.truetype('JOKERMAN.TTF', 27)
    code = ''
    for i in range(0, 5):
        num = random.randint(0, 55)
        code += s_list[num]
        huabi.text((i * 25 + 5, 5), s_list[num], font=font,
                   fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    io_img = io.BytesIO()
    huabu.save(io_img, 'png')
    request.session['yan'] = code.lower()

    # print(code.lower())
    return HttpResponse(io_img.getvalue(), 'images/png')


# 验证码是否正确
def yzm_if_not(request):
    q_yan = request.POST.get('yan')
    h_yan = request.session.get('yan')

    if q_yan == h_yan:  # 0正确  1错误
        con = {
            'data': '',
            'status': 0
        }
    else:
        con = {
            'data': '验证码错误！',
            'status': 1
        }
    return HttpResponse(json.dumps(con), content_type='application/json')


# 登录界面
def login(request):
    return render(request, 'shop/login.html')


# 登陆成功页面
def login_1(request):
    return render(request, 'shop/login_1.html')


# 执行登陆
def do_login(request):
    md5 = hashlib.md5()
    md5.update(request.POST.get('pswd').encode('utf-8'))
    password = md5.hexdigest()
    username = request.POST.get('username')
    q_yan = request.POST.get('yanzheng')
    # print('前端验证码'+request.POST.get('yanzheng'))
    h_yan = request.session.get('yan')
    info = models.User.objects.filter(username=username).first()
    try:
        # 查找到该用户的对象
        obj = models.User.objects.get(username=username)  # 没错误说明查到了该对象
        if obj.password == password:
            if q_yan == h_yan:  # 0正确  1错误
                print('验证码正确')
                request.session['user_id'] = info.id
                con = {
                    'data': '登录成功！',
                    'status': 0
                }
                return HttpResponse(json.dumps(con), content_type='application/json')
            else:
                con = {  # 验证码错误
                    'data': '验证码错误',
                    'status': 2
                }
                print(q_yan + '前端验证码')
                print(h_yan + '后台验证码')
                return HttpResponse(json.dumps(con), content_type='application/json')
        else:
            con = {
                'data': '用户名或密码错误',
                'status': 1
            }
            return HttpResponse(json.dumps(con), content_type='application/json')
    except:
        con = {
            'data': '用户名或密码错误',
            'status': 1
        }
        return HttpResponse(json.dumps(con), content_type='application/json')


# 显示主页
def index(request):
    fol_obj = models.Home_floor.objects.filter()
    type_list = models.Classify.objects.filter(Parentid=0)

    con = {
        'data': fol_obj,
        'type_list': type_list,

    }

    return render(request, 'shop/index.html', con)


# 列表详情页
def list_comm(request):
    # 检索
    p = request.GET.get('p', 1)
    name = request.GET.get('name', '')
    type_id = request.GET.get('tid', 0)

    # 用于拼接检索条件
    q = Q()
    q.connector = 'and'
    q.children.append(('disabled', 0))  # 删除的不再显示
    where_page = []  # 记录搜索条件，用于拼接分页链接

    if name != '':
        q.children.append(('name', name))  #
        where_page.append('name=' + name)
    if type_id != 0:
        q.children.append(('types_id', type_id))
        where_page.append('tid=' + type_id)

    page_url = '&'.join(where_page)  # 拼接

    data = models.Commodity.objects.filter(status='0')

    # 分页
    page = Paginator(data, 8)
    data = page.page(p)

    con = {
        'data': data,
        'page_url': page_url,

    }
    return render(request, 'shop/list.html', con)


def getParentId(type_id, lis):
    info = models.Classify.objects.filter(id=type_id).first()
    if info.Parentid != 0:
        lis.append((info.Parentid, info.name))
        getParentId(info.Parentid, lis)
    else:
        lis.append((info.Parentid, info.name))
    return lis


# 商品详情页
def show_details(request, id):
    data = models.Commodity.objects.filter(id=id).first()

    # 分类id  面包屑
    lis = getParentId(data.classify_id_id, [])
    lis.reverse()
    con = {
        'data': data,
        'lis': lis,
    }

    print('面包屑')
    print(lis)

    return render(request, 'shop/show_details.html', con)


# 添加购物车
def add_cart(request):
    comm_id = request.POST.get('id')
    comm_num = request.POST.get('num')

    user_id = request.session.get('user_id', 0)
    print('用户id')
    print(user_id)
    if user_id == 0:
        con = {
            'status': 1
        }
        print('还没登陆')
        return HttpResponse(json.dumps(con), content_type='application/json')

    info = models.Shopping_cart.objects.filter(commodity_id_id=comm_id,
                                               user_id_id=user_id).first()
    if info != None:
        models.Shopping_cart.objects.filter(commodity_id_id=comm_id,
                                            user_id_id=request.session.get('user_id')).update(
            number=F('number') + comm_num)
    else:
        cartObj = models.Shopping_cart()
        cartObj.commodity_id_id = comm_id
        cartObj.user_id_id = user_id
        cartObj.number = comm_num
        cartObj.checked = 0
        cartObj.save()

    con = {
        'status': 0,
    }
    # print()
    return HttpResponse(json.dumps(con), content_type='application/json')


# 显示购物车
def show_cart(request):
    user_id = request.session.get('user_id')

    cart_list = models.Shopping_cart.objects.filter(user_id=user_id)
    cart_list2 = models.Shopping_cart.objects.filter(user_id=user_id, checked=1)

    zongjia = 0
    for cart in cart_list2:
        # print(cart.number*float(cart.commodity_id.price))
        # print()
        zongjia = zongjia + cart.number * float(cart.commodity_id.price)
    print('zongjia')
    print(zongjia)
    con = {
        'cart_list': cart_list,
        'zongjia': zongjia,
    }
    return render(request, 'shop/order_step1.html', con)


# 实时更新购物车
def update_show_cart(request):
    cart_id_str = request.POST.get('cart_id_lis')
    print(cart_id_str)
    zongjia = 0

    maxlis = []  # 全部的id
    minlis = []  # 选中的id

    # 先跟新当前商品的数量
    num = request.POST.get('num')
    id = request.POST.get('id')
    models.Shopping_cart.objects.filter(id=id).update(number=num)

    if cart_id_str == '':  # 如果一个都没选，则将状态都置为0
        print('空')
        models.Shopping_cart.objects.filter().update(checked=0)

        con = {
            'data': zongjia,
        }
        return HttpResponse(json.dumps(con), content_type='application/json')

    else:
        for i in models.Shopping_cart.objects.filter():
            maxlis.append(i.id)

        for i in cart_id_str.split(','):
            minlis.append(int(i))

        for i in minlis:
            for j in maxlis:
                if i == j:
                    maxlis.remove(j)  # 除去选中的，剩下未选中的

        print(maxlis)
        print(minlis)
        for cart_id in maxlis:  # 将未选中的状态置为0
            models.Shopping_cart.objects.filter(id=int(cart_id)).update(checked=0)

        for cart_id in minlis:  # 将选中的状态置为1
            models.Shopping_cart.objects.filter(id=int(cart_id)).update(checked=1)

        user_id = request.session.get('user_id')
        cart_list2 = models.Shopping_cart.objects.filter(user_id=user_id, checked=1)

        for cart in cart_list2:
            zongjia = zongjia + cart.number * float(cart.commodity_id.price)
        print('zongjia')
        print(zongjia)
        con = {
            'data': zongjia,
        }

        return HttpResponse(json.dumps(con), content_type='application/json')


# 删除购物车
def dell_show_cart(request):
    cart_id = request.POST.get('id')
    print('删除1')

    models.Shopping_cart.objects.filter(id=cart_id).delete()

    con = {
        'data': 0,
    }
    print('删除2')

    return HttpResponse(json.dumps(con), content_type='application/json')


# 结算页面1
def jiesuan(request):
    user_id = request.session.get('user_id')
    address = models.User_Receiving_Address.objects.filter(userid_id=user_id)
    zongjia = 0
    goods = models.Shopping_cart.objects.filter(checked=1)
    for cart in goods:
        zongjia = zongjia + cart.number * float(cart.commodity_id.price)
    con = {
        'data': address,
        'goods': goods,
        'zongjia': zongjia
    }

    return render(request, 'shop/order_step2.html', con)


# 添加订单表
def add_order_form(request):
    user_id = request.session.get('user_id')
    # 订单号
    danhao = 'USC' + str(time.time()).split('.')[0] + str(time.time()).split('.')[1] + str(user_id)

    zongjia = 0
    goods = models.Shopping_cart.objects.filter(checked=1)
    for cart in goods:
        zongjia = zongjia + cart.number * float(cart.commodity_id.price)

    order_from = models.Order_form()
    order_from.user_id_id = user_id
    order_from.code_num = danhao
    order_from.money = zongjia
    order_from.pay_money = zongjia
    order_from.status = 0
    order_from.pay_status = 0
    order_from.pay_type = '支付宝'
    order_from.save()

    con = {
        'data': 0
    }

    return HttpResponse(json.dumps(con), content_type='application/json')


# 结算页面2
def jiesuan2(request):
    user_id = request.session.get('user_id')
    order_from = models.Order_form.objects.filter(user_id_id=user_id, pay_status=0).first()

    # 订单号
    danhao = order_from.code_num

    zongjia = order_from.money

    con = {

        'danhao': danhao,
        'zongjia': zongjia
    }

    return render(request, 'shop/order_step3.html', con)
