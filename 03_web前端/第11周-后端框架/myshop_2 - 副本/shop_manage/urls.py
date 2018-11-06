from django.conf.urls import url
from . import views
import shop

urlpatterns = [
    url(r'^login/$', views.login, name='login_shop_manage'),
    url(r'^do_login/$', views.do_login, name='do_login_shop_manage'),
    url(r'^index/$', views.index, name='index_shop_manage'),
    url(r'^goods_add/$', views.goods_add, name='goods_add_shop_manage'),
    url(r'^goods_list/$', views.goods_list, name='goods_list_shop_manage'),
    url(r'^add_tyep/$', views.add_tyep, name='add_tyep_shop_manage'),
    url(r'^do_add_tyep/$', views.do_add_tyep, name='do_add_tyep_shop_manage'),
    url(r'^xiugai/$', views.xiugai, name='xiugai_shop_manage'),
    url(r'^update/$', views.update, name='update_shop_manage'),
    url(r'^dell/$', views.dell, name='dell_shop_manage'),
    url(r'^do_good_add/$', views.do_good_add, name='do_good_add_shop_manage'),
    url(r'^type_list/$', views.type_list, name='type_list_shop_manage'),
    url(r'^add_power/$', views.add_power, name='add_power_shop_manage'),
    url(r'^do_add_power/$', views.do_add_power, name='do_add_power_shop_manage'),
    url(r'^add_role/$', views.add_role, name='add_role_shop_manage'),
    url(r'^do_add_role/$', views.do_add_role, name='do_add_role_shop_manage'),
    url(r'^add_floor_comm/$', views.add_floor_comm, name='add_floor_comm_shop_manage'),
    url(r'^do_add_floor_comm/$', views.do_add_floor_comm, name='do_add_floor_comm_shop_manage'),
    url(r'^add_floor/$', views.add_floor, name='add_floor_shop_manage'),
    url(r'^do_add_floor/$', views.do_add_floor, name='do_add_floor_shop_manage'),

]