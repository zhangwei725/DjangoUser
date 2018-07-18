from django.conf.urls import url, include
from django.contrib import admin

from user_auth import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index, name='index'),
    url('users/', include('user_auth.urls')),
    url('captcha/', include('captcha.urls')),
    url('redi/', include('redi.urls')),

]
