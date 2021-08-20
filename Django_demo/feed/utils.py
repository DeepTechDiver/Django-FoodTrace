import random
import datetime
from feed import models
import time
import hashlib

# 随机生成token
def get_token():
    src = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()', 20))
    m2 = hashlib.md5()
    m2.update(src.encode("utf8"))
    return m2.hexdigest()

# 统计当前每个角色每天的订单提交量
def add_role_data(role):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    admin = models.role_date_data.objects.filter(date = now_time)
    if admin.count()==0:
        test1 = models.role_date_data(date = now_time,
                                      production = 0,
                                      bidders = 0,
                                      transport = 0,
                                      sale = 0,
                                      consume = 0)
        test1.save()
        test2 = models.role_date_data.objects.get(date = now_time)
        if role=='production':
            test2.production = test2.production + 1
            test2.save()
        elif role == 'bidders':
            test2.bidders = test2.bidders + 1
            test2.save()
        elif role == 'transport':
            test2.transport = test2.transport + 1
            test2.save()
        elif role == 'sale':
            test2.sale = test2.sale + 1
            test2.save()
        else:
            test2.consume = test2.consume + 1
            test2.save()
    else:
        test2 = models.role_date_data.objects.get(date = now_time)
        if role=='production':
            test2.production = test2.production + 1
            test2.save()
        elif role == 'bidders':
            test2.bidders = test2.bidders + 1
            test2.save()
        elif role == 'transport':
            test2.transport = test2.transport + 1
            test2.save()
        elif role == 'sale':
            test2.sale = test2.sale + 1
            test2.save()
        else:
            test2.consume = test2.consume + 1
            test2.save()

def get_time(num):
    timeArray = time.localtime(int(num/1000))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime