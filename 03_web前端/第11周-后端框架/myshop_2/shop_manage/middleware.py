from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, HttpResponseRedirect, reverse, render
from django.conf import settings
from shop_manage.models import Power
import re


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        m = [settings.LOGIN_URL]
        uid = request.session.get('uid', 0)
        # print('-------------------')
        # print(uid)
        url = request.path
        name = re.match(r'^/shop_manage/?$', url)
        # print(request.path)
        # print(m)
        # if uid == 0 and request.path not in m:
        #     return render(request, 'shop_manage/login.html')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        name = re.match(r'^/(shop)?|(shop_manage)?/?$', request.path).group(1)
        url = request.path
        p = re.compile(r'^/shop_manage/')
        is_ = re.match(p, url)
        if is_ != None:
            # print(request.path)
            # print(request.resolver_match.url_name)
            pass_list = ['login_shop_manage', 'index_shop_manage']
            power_list = request.session.get('user_power')
            urlname = request.resolver_match.url_name
            info = Power.objects.filter(urlname=urlname).first()
            if info != None:
                if info.id not in power_list:
                    return HttpResponse('您没有权限')
