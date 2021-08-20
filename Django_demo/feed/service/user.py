import json
from feed import models,results,utils

def login(dict):
    admin = models.user.objects.filter(username = dict['username'])
    if admin.count() == 0:
        return results.user_none_error
    else:
        test1 = models.user.objects.get(username = dict['username'])
        token = test1.token
        if dict['password'] == test1.password:
            return_result = json.dumps({
                'code':200,
                'data':{'token': token}
            })
            return return_result
        else:
            return results.user_password_error

def create(dict):
    username = dict['username']
    password = dict['password']
    address = dict['address']
    role = dict['role']
    token = utils.get_token()
    admin = models.user(username = username,
                        password = password,
                        address = address,
                        role = role,
                        token = token)
    admin.save()
    return results.user_create_success

# 查询个人信息
def personal_info(dict):
    admin = models.user.objects.get(username = dict['username'])
    data = {
        'username' : admin.username,
        'password' : admin.password,
        'address' : admin.address,
        'role': admin.role
    }
    return_result = {
        'code':200,
        'data':data
    }
    print(return_result)
    return json.dumps(return_result)

#
def user_info_change(dict):
    print(dict)
    username = dict['username']
    password_change = dict['password']
    address_change = dict['address']
    role_change = dict['role_change']
    password = dict['password']
    address = dict['address']
    role = dict['role']
    if password_change == True:
        admin = models.user.objects.get(username = username)
        admin.password = password
        admin.save()
    if address_change == True:
        admin = models.user.objects.get(username = username)
        admin.address = address
        admin.save()
    if role_change == True:
        admin = models.user.objects.get(username = username)
        admin.role = role
        admin.save()
    return_result = json.dumps({
        'code':200,
        'data':{'message':'修改成功'}
    })
    return return_result