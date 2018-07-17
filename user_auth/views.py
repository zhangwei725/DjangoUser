from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user_auth.models import User


# 有些时候需要在系统的对象进行扩展
#  继承 AbstractUser  一般适合新的项目
# 用户内置用户修改  注意
#  AUTH_USER_MODEL = 'user_auth.User'


# 常用操作
# create_user
# authenticate
# login
# logout
# is_authenticated

def index(request):
    return render(request, 'index.html')


def login_view(request):
    context = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = authenticate(username=username, password=password)
                if user:
                    # 记住用户的登录状态
                    login(request, user)
                    return redirect('/')
                else:
                    context = {'msg': '账号密码错误'}
            except:
                context = {'msg': '登录失败!!!'}
        else:
            context = {'msg': '账号密码不能为空'}
    return render(request, 'login.html', context)


# ctrl + d
def register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if password == confirm_password:
            users = User.objects.filter(username=username)
            if not users:
                try:
                    user = User.objects.create_user(username=username, password=password, email=email, phone=phone)
                    login(request, user)
                    # 邮箱激活
                    return redirect('/')
                except:
                    context['msg'] = '注册失败'
            else:
                context['msg'] = '用户名已存在'
        else:
            context['msg'] = '两次密码输入不一致'
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
