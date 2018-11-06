from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^demo/$', views.demo, name='demo'),
    # 显示主页
    url(r'^$', views.index, name='index'),
    # 显示添加页面
    url(r'^add/$', views.add, name='add'),
    # 执行添加操作
    url(r'^do_add/$', views.do_add, name='do_add'),

    # 显示学生信息页面
    url(r'^show/$', views.show, name='show'),

    # 显示注册页面
    url(r'^res/$', views.res, name='res'),

    # 执行注册操作
    url(r'^do_res/$', views.do_res, name='do_res'),

    # 显示登录页面
    url(r'^login/$', views.login, name='login'),

    # 执行登录操作
    url(r'^do_login/$', views.do_login, name='do_login'),

    # 注销
    url(r'^logout/$', views.logout, name='logout'),

    # 阅读
    url(r'^yuedu/$', views.yuedu, name='yuedu'),

    # 娱乐
    url(r'^yule/$', views.yule, name='yule'),

    # 检测
    url(r'^jiance/$', views.jiance, name='jiance'),

    #删除
    url(r'^dell/(?P<id>\d+)$', views.dell, name='dell'),


    # 更新
    url(r'^update/$', views.update, name='update'),

    url(r'^xiugai/$', views.xiugai, name='xiugai'),

]
