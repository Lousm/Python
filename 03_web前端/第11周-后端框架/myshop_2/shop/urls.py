from django.conf.urls import url
from . import views,pay

urlpatterns = [
    url(r'^res/$', views.res, name='res_shop'),
    url(r'^do_res/$', views.do_res, name='do_res_shop'),
    url(r'^res_1/$', views.res_1, name='res_1_shop'),
    url(r'^username1/$', views.username1, name='username1_shop'),
    #生成验证码
    url(r'^yzm/$', views.yzm, name='yzm_shop'),
    #验证码是否正确
    url(r'^yzm_if_not/$', views.yzm_if_not, name='yzm_if_not_shop'),
    url(r'^login/$', views.login, name='login_shop'),
    url(r'^login_1/$', views.login_1, name='login_1_shop'),
    url(r'^do_login/$', views.do_login, name='do_login_shop'),

    #显示主页
    url(r'^index/$', views.index, name='index_shop'),

    #列表详情
    url(r'^list/$', views.list_comm, name='list_comm_shop'),

    #商品详情
    url(r'^show_details/(?P<id>\d+)$', views.show_details, name='show_details_shop'),

    #支付
    url(r'^dopay/$', pay.dopay, name='dopay_shop'),

    # url(r'^dopay_1/$', pay.dopay_1, name='dopay_1_shop'),

    #添加购物车
    url(r'^add_cart/$', views.add_cart, name='add_cart_shop'),

    #购物车页面
    url(r'^show_cart/$', views.show_cart, name='show_cart_shop'),

    #结算页面1
    url(r'^jiesuan/$', views.jiesuan, name='jiesuan_shop'),

    #结算页面2
    url(r'^jiesuan2/$', views.jiesuan2, name='jiesuan2_shop'),

    #实时更新购物车表
    url(r'^update_show_cart/$', views.update_show_cart, name='update_show_cart_shop'),

    #删除购物车
    url(r'^dell_show_cart/$', views.dell_show_cart, name='dell_show_cart_shop'),

    #添加订单表
    url(r'^add_order_form/$', views.add_order_form, name='add_order_form_shop'),

    url(r'^return_url/$',pay.return_url),


]