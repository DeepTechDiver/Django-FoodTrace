import json
from feed import models
from django.http import HttpResponse
from feed.service import contract_feed
import requests

def token_username(request):
    token = request.COOKIES['token']
    user = models.user.objects.get(token = token)
    return_result = json.dumps({
        'code':200,
        'data':user.username
    })
    return HttpResponse(return_result)

def get_user_role(dict):
    admin = models.user.objects.get(token = dict['token'])
    address = admin.address
    data = {
        "groupId": "1",
        "user": address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "getUserRole",
        "funcParam": [address],
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
    print(res)
    if res.status_code == 200:
        role = json.loads(res.text)[0]
        return_result = json.dumps({
            'code': 200,
            'data': role
        })
        return return_result
    else:
        return_result = json.dumps({
            'code': res.status_code,
            'data': res.text
        })
        return return_result

def user_info():
    objects = models.user.objects.all().order_by('id')
    return_data = []
    for i in objects:
        address = i.address
        data = {
            "groupId": "1",
            "user": address,
            "contractName": contract_feed.feed_name,
            # "contractPath": "FeedTrace",
            "version": "",
            "funcName": "getUserRole",
            "funcParam": [address],
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
        real_role = json.loads(res.text)[0]
        return_data.append({'username':i.username,
                            'password':i.password,
                            'address':i.address,
                            'role':i.role,
                            'real_role':real_role})
    return_result = json.dumps({
        'code':200,
        'data':return_data
    })
    return return_result

def role_change(dict):
    # 查询原来的role
    root = models.user.objects.get(username = '123')
    root_address = root.address
    address = dict['address']
    role = dict['real_role']
    data = {
        "groupId": "1",
        "user": root_address,
        "contractName": contract_feed.feed_name,
        # "contractPath": "FeedTrace",
        "version": "",
        "funcName": "changeRole",
        "funcParam": [address, role],
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


