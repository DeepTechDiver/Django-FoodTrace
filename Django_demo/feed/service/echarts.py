import json
from feed import models
import datetime

def echarts12():
    before_7_days = []
    # 生产
    production = []
    # 收购
    bidders = []
    # 运输
    transport = []
    # 销售
    sale = []
    # 消费
    consume =[]
    for i in range(1,8)[::-1]:
        before_7_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
    for i in before_7_days:
        test = models.role_date_data.objects.get(date = i)
        production.append(test.production)
        bidders.append(test.bidders)
        transport.append(test.transport)
        sale.append(test.sale)
        consume.append(test.consume)
    data = {
        'date' : before_7_days,
        'production' : production,
        'bidders' : bidders,
        'transport' : transport,
        'sale':sale,
        'consume':consume
    }
    return_result = json.dumps({
        'code':200,
        'data':data
    })
    return return_result

def echarts34():
    before_7_days = []
    data = []
    # 生产
    production = []
    # 收购
    bidders = []
    # 运输
    transport = []
    # 销售
    sale = []
    # 消费
    consume =[]
    for i in range(1,8)[::-1]:
        before_7_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
    for i in before_7_days:
        test = models.role_date_data.objects.get(date = i)
        production.append(test.production)
        bidders.append(test.bidders)
        transport.append(test.transport)
        sale.append(test.sale)
        consume.append(test.consume)
    data.append(production)
    data.append(bidders)
    data.append(transport)
    data.append(sale)
    data.append(consume)
    dict = {
        'date' : before_7_days,
        'data' : data
    }
    return_result = json.dumps({
        'code':200,
        'data':dict
    })
    return return_result