from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^test/$', views.test, name='test'),
    url(r'^$',views.index,name='index'),
    url(r'^heard/$',views.heard,name='heard'),
    url(r'^hbf/$', views.hbf, name='hbf'),
    url(r'^ext/$', views.ext, name='ext'),

    #小括号传参
    url(r'^a1/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.a1, name='year'),

    #分组命名匹配（形参位置不固定，自需要名字对应就行）
    url(r'^a2/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/(?P<s>[0-9]{2})/$', views.a2, {'name':'小明'}, name='zxc'),

    #http://10.10.91.184:8000/zhihu/a3/?name=asd&age=132456
    url(r'^a3/$', views.a3),

    #前台登陆页面
    url(r'^login/$', views.login, name='login'),

    #注册页面
    url(r'^res/$', views.res, name='res'),

    #登录
    url(r'^do_login/$', views.do_login, name='do_login'),

]