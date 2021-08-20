"""Django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from feed import views
from feed.service import main

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户登录
    path('user/login',views.login),
    # 注册用户
    path('user/create',views.create),
    # 获取用户对应的角色
    path('get_user_role',views.get_user_role),
    # 登录页面时通过token获取usename
    path('token_username',main.token_username),
    # 在main展现的所有用户
    path('main/user_info',views.user_info),
    # root用户对用户的角色进行修改
    path('main/role_change',views.role_change),
    # 创建订单时，获取订单ID
    path('get_id',views.get_id),
    # 个人信息
    path('personal_info',views.personal_info),
    # echart数据请求
    path('echarts12',views.echarts12),
    path('echarts34',views.echarts34),
    # 提交生产商订单
    path('producers_order',views.producers_order),
    # 提交收购商订单
    path('bidders_order',views.bidders_order),
    # 提交运输商订单
    path('shippers_order',views.shippers_order),
    # 提交销售商订单
    path('sellers_order',views.sellers_order),
    # 获取生产商所有订单
    path('get_producers_order',views.get_producers_order),
    # 获取收购商所有订单
    path('get_bidders_order',views.get_bidders_order),
    # 获取运输商所有订单
    path('get_shippers_order',views.get_shippers_order),
    # 获取销售商所有订单
    path('get_sellers_order',views.get_sellers_order),
    # 获取id的食品信息
    path('get_id_info',views.get_id_info),
    # 通过id查询所有信息
    path('id_get_all',views.id_get_all),
    # 修改用户信息
    path('user_info_change',views.user_info_change)
]
