from django.conf.urls import url
from . import views

urlpatterns = [
    # 显示添加页面
    url(r'^res/$', views.res, name='res'),
    #执行添加操作
    url(r'^do_res/$', views.do_res, name='do_res'),

    #显示登录页面
    url(r'^login/$', views.login, name='login'),
    #用户名密码错误页面
    url(r'^login_error/$', views.login_error, name='login_error'),
    #执行登录操作
    url(r'^do_login/$', views.do_login, name='do_login'),

    url(r'^$', views.index, name='index'),
    # 注销
    url(r'^logout/$', views.logout, name='logout'),

    # 显示个人信息
    url(r'^xinxi/$', views.xinxi, name='xinxi'),

    # 保存个人信息
    url(r'^do_xinxi/$', views.do_xinxi, name='do_xinxi'),

    # 显示欢迎小标题
    url(r'^huanying/$', views.huanying, name='huanying'),

]
