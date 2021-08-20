import json
from feed.service import contract_feed
from feed import models,utils
import requests
from django.http import HttpResponse

def get_id(dict):
    user = models.user.objects.get(username = dict['username'])
    name = dict['name']
    feedType = dict['feedType']
    data = {
        "groupId": "1",
        "user": user.address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "createFeed",
        "funcParam": [name, feedType],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    output = json.loads(res.text)['output']
    id = int(output,16)
    data = {
        "groupId": "1",
        "user": user.address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "getFeed",
        "funcParam": [id],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    feedname = json.loads(res.text)[0]
    return_result = json.dumps({
        'code':200,
        'data':{'id':id,'feedname':feedname}
    })
    return HttpResponse(return_result)

def producers_order(dict):
    feedNo = dict['id']
    feedname = dict['feedname']
    company = dict['company']
    people = dict['people']
    phone = dict['phone']
    username = dict['username']
    user = models.user.objects.get(username = username)
    data = {
        "groupId": "1",
        "user": user.address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "Produces",
        "funcParam": [feedNo,feedname,company,people,phone],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    if res.status_code == 200:
        utils.add_role_data('production')
        message = json.loads(res.text)['message']
        return_result = json.dumps({
            'code':200,
            'data':message
        })
        return return_result
    else:
        return_result = json.dumps({
            'code': res.status_code,
            'data': res.text
        })
        return return_result

def bidders_order(dict):
    username = dict['username']
    feedNo = dict['id']
    customer = dict['customer']
    people = dict['people']
    phone = dict['phone']
    user = models.user.objects.get(username = username)
    data = {
        "groupId": "1",
        "user": user.address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "Buy",
        "funcParam": [feedNo,customer,people,phone],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    if res.status_code == 200:
        utils.add_role_data('bidders')
        message = json.loads(res.text)['message']
        return_result = json.dumps({
            'code':200,
            'data':message
        })
        return return_result
    else:
        return_result = json.dumps({
            'code': res.status_code,
            'data': res.text
        })
        return return_result

def shippers_order(dict):
    username = dict['username']
    feedNo = dict['id']
    car_num = dict['car_num']
    form_place = dict['form_place']
    to_place = dict['to_place']
    people = dict['people']
    phone = dict['phone']
    user = models.user.objects.get(username = username)
    data = {
        "groupId": "1",
        "user": user.address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "Transport",
        "funcParam": [feedNo,car_num,form_place,to_place,people,phone],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    if res.status_code == 200:
        utils.add_role_data('transport')
        message = json.loads(res.text)['message']
        return_result = json.dumps({
            'code':200,
            'data':message
        })
        return return_result
    else:
        return_result = json.dumps({
            'code': res.status_code,
            'data': res.text
        })
        return return_result

def sellers_order(dict):
    username = dict['username']
    feedNo = dict['id']
    feedname = dict['feedname']
    weight = dict['weight']
    price = dict['price']
    day = dict['day']
    place = dict['place']
    people = dict['people']
    phone = dict['phone']
    user = models.user.objects.get(username = username)
    data = {
        "groupId": "1",
        "user": user.address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "Sale",
        "funcParam": [feedNo,feedname,weight,price,day,place,people,phone],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    if res.status_code == 200:
        utils.add_role_data('sale')
        message = json.loads(res.text)['message']
        return_result = json.dumps({
            'code':200,
            'data':message
        })
        return return_result
    else:
        return_result = json.dumps({
            'code': res.status_code,
            'data': res.text
        })
        return return_result

def get_producers_order(dict):
    user = models.user.objects.get(token = dict['token'])
    results = []
    id_list = get_all_id()
    for i in id_list[::-1]:
        data = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getProduce",
            "funcParam": [i],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[6] = utils.get_time(result[6])
        if result[6] == '1970-01-01 08:00:00':
            continue
        demo = {
            'id':result[0],
            'feedname':result[2],
            'company' : result[3],
            'people' : result[4],
            'phone' : result[5],
            'date' : result[6],
            'address' : result[7]
        }
        results.append(demo)
    return_result = json.dumps({
        'code':200,
        'data':results
    })
    return HttpResponse(return_result)

def get_bidders_order(dict):
    user = models.user.objects.get(token = dict['token'])
    results = []
    id_list = get_all_id()
    for i in id_list[::-1]:
        data = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getBuy",
            "funcParam": [i],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[5] = utils.get_time(result[5])
        if result[5] == '1970-01-01 08:00:00':
            continue
        demo = {
            'id':result[0],
            'customer':result[2],
            'people' : result[3],
            'phone' : result[4],
            'date' : result[5],
            'address' : result[6]
        }
        results.append(demo)
    return_result = json.dumps({
        'code':200,
        'data':results
    })
    return HttpResponse(return_result)

def get_shippers_order(dict):
    user = models.user.objects.get(token = dict['token'])
    results = []
    id_list = get_all_id()
    for i in id_list[::-1]:
        data = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getTransport",
            "funcParam": [i],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[7] = utils.get_time(result[7])
        if result[7] == '1970-01-01 08:00:00':
            continue
        demo = {
            'id':result[0],
            'car_num':result[2],
            'form_place':result[3],
            'to_place':result[4],
            'people' : result[5],
            'phone' : result[6],
            'date' : result[7],
            'address' : result[8]
        }
        results.append(demo)
    return_result = json.dumps({
        'code':200,
        'data':results
    })
    return HttpResponse(return_result)

def get_sellers_order(dict):
    user = models.user.objects.get(token = dict['token'])
    results = []
    id_list = get_all_id()
    for i in id_list[::-1]:
        data = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getSale",
            "funcParam": [i],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[9] = utils.get_time(result[9])
        if result[9] == '1970-01-01 08:00:00':
            continue
        demo = {
            'id':result[0],
            'weight':result[3],
            'price':result[4],
            'day':result[5],
            'place':result[6],
            'people' : result[7],
            'phone' : result[8],
            'date' : result[9],
            'address' : result[10]
        }
        results.append(demo)
    return_result = json.dumps({
        'code':200,
        'data':results
    })
    return HttpResponse(return_result)

def get_id_info(dict):
    username = dict['username']
    id = dict['id']
    user = models.user.objects.get(username = username)
    data = {
        "groupId": "1",
        "user": user.address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "getFeed",
        "funcParam": [id],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    feedname = json.loads(res.text)[0]
    result_result = json.dumps({
        'code':200,
        'data':feedname
    })
    return result_result

def id_get_all(dict):
    username = dict['username']
    feedNo = dict['search']
    results = []
    user = models.user.objects.get(username = username)
    id_list = get_all_id()
    if int(feedNo) in id_list:
        data_1 = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getProduce",
            "funcParam": [feedNo],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data_1).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[6] = utils.get_time(result[6])
        demo = {
            'feedname':result[2],
            'company' : result[3],
            'people' : result[4],
            'phone' : result[5],
            'date' : result[6],
            'address' : result[7]
        }
        results.append(demo)
        data_2 = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getBuy",
            "funcParam": [feedNo],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data_2).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[5] = utils.get_time(result[5])
        demo = {
            'customer':result[2],
            'people' : result[3],
            'phone' : result[4],
            'date' : result[5],
            'address' : result[6]
        }
        results.append(demo)
        data_3 = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getTransport",
            "funcParam": [feedNo],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data_3).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[7] = utils.get_time(result[7])
        demo = {
            'car_num':result[2],
            'form_place':result[3],
            'to_place':result[4],
            'people' : result[5],
            'phone' : result[6],
            'date' : result[7],
            'address' : result[8]
        }
        results.append(demo)
        data_4 = {
            "groupId": "1",
            "user": user.address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getSale",
            "funcParam": [feedNo],
            "contractAddress": contract_feed.feed_address,
            "contractAbi": contract_feed.feed_abi,
            "useAes": False,
            "useCns": False,
            "cnsName": ""
        }
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                            headers = headers,
                            data = json.dumps(data_4).replace("False", "false").replace("True", "true"))
        result = json.loads(res.text)
        result[9] = utils.get_time(result[9])
        demo = {
            'weight':result[3],
            'price':result[4],
            'day':result[5],
            'place':result[6],
            'people' : result[7],
            'phone' : result[8],
            'date' : result[9],
            'address' : result[10]
        }
        results.append(demo)
        utils.add_role_data('consume')
        return_results = json.dumps({
            'code':200,
            'data':results
        })
        return return_results
    else:
        return_results = json.dumps({
            'code':201,
            'data':{'context':'未找到该订单'}
        })
        return return_results

def get_all_id():
    data = {
        "groupId": "1",
        "user": 0xbd762eb12badd1925f71f26a8fcd5a02f0335e34,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "getid",
        "funcParam": [],
        "contractAddress": contract_feed.feed_address,
        "contractAbi": contract_feed.feed_abi,
        "useAes": False,
        "useCns": False,
        "cnsName": ""
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url='http://192.168.145.148:5002/WeBASE-Front/trans/handle',
                        headers = headers,
                        data = json.dumps(data).replace("False", "false").replace("True", "true"))
    # id_list = json.loads(res.text[0])
    # print(id_list)

    # print(res.json())
    id_list = res.json()[0]
    return id_list