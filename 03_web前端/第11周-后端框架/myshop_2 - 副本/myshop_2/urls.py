"""myshop_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from .upload import upload_image
from django.conf import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^hello/', include('hello.urls')),
                  url(r'^zhihu/', include('zhihu.urls')),
                  url(r'^blog/', include('blog.urls')),
                  url(r'^login_res/', include('login_res.urls')),
                  url(r'^student_manage/', include('student_manage.urls')),
                  url(r'^shop/', include('shop.urls')),
                  url(r'^shop_manage/', include('shop_manage.urls')),
                  url(r'^shop_manage/uploads/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
