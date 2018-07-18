from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

"""
重定向
    1> 支持站内跟站外
    2> 跳转的路径可以相对路径也可是绝对路径

# /xx/xx/  相对路径
# http://域名/path?参数 /绝对路径


HttpResponseRedirect
redirect
"""


def redi1(request):
    # 跳转站内的路径
    return HttpResponseRedirect('/')
    # 跳转站内的路径带参数
    # return HttpResponseRedirect('/user/change/?uid=1')
    #  站外不带参数
    # return HttpResponseRedirect('https://www.baidu.com/')
    #  站外带参数1
    # return HttpResponseRedirect('http://gank.io/api/data/%E7%A6%8F%E5%88%A9/20/3/')
    #  站外跳转带参数2
    # return HttpResponseRedirect('https://www.apiopen.top/satinApi?type=1&page=1')


"""
redirect(to,*args,**kwargs)
参数说明
to    
1>  直接使用相对路径或者绝对路径
2>  使用别名 ,reverse('命名空间:别名')
  
3> reverse 方向解析 
    语法格式
   reverse('命名空间:别名',*args ,kwargs)
    参数一
       include('user_auth.urls', namespace='user')
       url(r'login/', views.login_view, name='login'),
       也可以直接使用别名
       # 注意不要使用命名空间
       return redirect(reverse('login'))
    参数2 在路径里传递参数
       url(r'list/(\d+)/(\d+)/', views.list, name='list'),
       reverse(list,args=(1,2))
    参数3   
       url(r'list2/(?P<uid>\d+)', views.list2, name='list2'), 
       reverse(list,kwargs={'uid':'10'})
     reverse('/index/')
    
    区别   
    render   地址栏不会发生改变 相当界面整体刷新,
    redirect 地址发生改变,
"""


def redi2(request):
    # return redirect('/')
    # return redirect('https://www.apiopen.top/satinApi?type=1&page=2')
    # return redirect('/users/login/')
    return redirect(reverse('login'))


def redi3(request):
    path = reverse('list2', kwargs={'uid': '1'})
    # return redirect(reverse('list', args=(1, 10)))
    return redirect(reverse('list2', kwargs={'uid': '10'}))
