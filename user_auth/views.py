from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    # 生成随机的字符窜
    key = CaptchaStore.generate_key()
    # 根据随机字符生成相应的图片地址
    captcha_img_url = captcha_image_url(key)
    context.update(captcha_key=key, captcha_img_url=captcha_img_url)
    if request.method == 'POST':

        key = request.POST.get('captcha_key')
        code = request.POST.get('validate_code')
        # 获取用户输入的验证码
        captcha = CaptchaStore.objects.filter(hashkey=key).values_list('challenge', flat=True)[0]
        if not code:
            context.update(msg='验证不能为空')
        else:
            if captcha and captcha == code.upper():
                username = request.POST.get('username')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                if password == confirm_password:
                    users = User.objects.filter(username=username)
                    if not users:
                        try:
                            user = User.objects.create_user(username=username, password=password, email=email,
                                                            phone=phone)
                            login(request, user)
                            # 邮箱激活
                            return redirect('/')
                        except:
                            context['msg'] = '注册失败'
                    else:
                        context['msg'] = '用户名已存在'
                else:
                    context['msg'] = '两次密码输入不一致'
            else:
                context.update(msg='验证输入不正确')
    #  生成验证码
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def captcha(request):
    # 生成随机的字符窜
    key = CaptchaStore.generate_key()
    # 根据随机字符生成相应的图片地址
    img_url = captcha_image_url(key)
    return render(request, 'index.html', {'img_url': img_url})


# json 客服端与服务器通用的一种交换数据的格式

# 序列化   生成json数据
# 反序列化  解析json数据
#  python不支持类转化成json数据
"""

{}
[]

服务器响应json数据--->   数组      就对象


python              json数据  {'key':value,key:value}   
数字类型            数字类型
字符串              字符串类型
字典                   对象
列表                   数组
None                   null
bool                   Boolean
"""

import json


# input
def refresh_code(request):
    # 生成随机的字符窜
    key = CaptchaStore.generate_key()
    # 根据随机字符生成相应的图片地址
    img_url = captcha_image_url(key)
    #  序列化  就字典生成json数据
    result = json.dumps({'captcha_key': key, 'captcha_img_url': img_url})
    return HttpResponse(result, content_type='application/json')


"""
必须登录之后才能去访问
如果没登录跳转登录的界面
"""


#
# def test():
#     user = User.objects.get(id=1)
#     user.userprofile.phone


# 局部跳转
@login_required
def change(request):
    try:
        user = User.objects.get(id=1)
        user.set_password('123456')
    except User.DoesNotExist:
        pass
    return HttpResponse('修改成功')


def list(request, page, size):
    return HttpResponse(page)


def list2(request, uid):
    return HttpResponse(uid)
