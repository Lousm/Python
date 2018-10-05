from django.conf.urls import url
from  . import  views

urlpatterns = [
    #显示添加页面
    url(r'^add/$',views.add,name='add'),
    #执行添加操作
    url(r'^do_add/$',views.do_add,name='do_add'),
    #执行显示操作
    url(r'^shuju/$',views.shuju,name='shuju'),
    url(r'^input_id/$',views.input_id,name='input_id'),
    #执行删除操作
    url(r'^dell/(?P<id>\d+)$',views.dell,name='dell'),

    url(r'^edit/(?P<id>\d+)$',views.edit,name='edit'),
    #执行更新操作
    url(r'^update/$',views.update,name='update'),
]