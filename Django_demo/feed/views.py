from django.shortcuts import render
import json
from django.http import HttpResponse
from feed.service import user,main,role,echarts
from feed import utils

# 登录接口
def login(request):
    body = json.loads(request.body)
    return HttpResponse(user.login(body))

# 创建用户接口
def create(request):
    body = json.loads(request.body)
    return HttpResponse(user.create(body))

# 获取用户角色接口
def get_user_role(request):
    body = json.loads(request.body)
    return HttpResponse(main.get_user_role(body))

# 查询所有用户信息的接口
def user_info(request):
    return HttpResponse(main.user_info())

def role_change(request):
    body = json.loads(request.body)
    return HttpResponse(main.role_change(body))

# 获取feed的id
def get_id(request):
    body = json.loads(request.body)
    return HttpResponse(role.get_id(body))

def personal_info(request):
    body = json.loads(request.body)
    return HttpResponse(user.personal_info(body))

def echarts12(request):
    return HttpResponse(echarts.echarts12())

def echarts34(request):
    return HttpResponse(echarts.echarts34())

def producers_order(request):
    body = json.loads(request.body)
    return HttpResponse(role.producers_order(body))

def bidders_order(reqeust):
    body = json.loads(reqeust.body)
    return HttpResponse(role.bidders_order(body))

def shippers_order(request):
    body = json.loads(request.body)
    return HttpResponse(role.shippers_order(body))

def sellers_order(request):
    body = json.loads(request.body)
    return HttpResponse(role.sellers_order(body))

def get_producers_order(request):
    body = json.loads(request.body)
    return HttpResponse(role.get_producers_order(body))

def get_bidders_order(request):
    body = json.loads(request.body)
    return HttpResponse(role.get_bidders_order(body))

def get_shippers_order(request):
    body = json.loads(request.body)
    return HttpResponse(role.get_shippers_order(body))

def get_sellers_order(request):
    body = json.loads(request.body)
    return HttpResponse(role.get_sellers_order(body))

def id_get_all(request):
    body = json.loads(request.body)
    return HttpResponse(role.id_get_all(body))

def get_id_info(request):
    body = json.loads(request.body)
    return HttpResponse(role.get_id_info(body))

def user_info_change(request):
    body = json.loads(request.body)
    return HttpResponse(user.user_info_change(body))