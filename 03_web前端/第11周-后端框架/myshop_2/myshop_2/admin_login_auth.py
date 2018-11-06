from django.shortcuts import HttpResponseRedirect
# from django.utils.deprecation import MiddlewareMixin
from django.utils.deprecation import MiddlewareMixin

# 自定义中间件类
class AdminAuthMiddleWare(MiddlewareMixin):

    # 实现process_request方法
    def process_request(self, request):
        # 获取session内用户登录标识
        uid=request.session.get('uid',0)
        # 判断用户未登录，并且访问路径不是登录页面
        if uid==0 and request.path!='/shop_manage/login/' :
            return HttpResponseRedirect('/shop_manage/login/')  # 跳转到登录页
