from django.conf.urls import url

from user_auth import views

urlpatterns = [
    url(r'login/', views.login_view, name='login'),
    url(r'register/', views.register, name='register'),
    url(r'logout/', views.logout_view, name='logout'),
    url(r'captcha/', views.captcha, name='captcha'),
    url(r'refresh/', views.refresh_code),
]
