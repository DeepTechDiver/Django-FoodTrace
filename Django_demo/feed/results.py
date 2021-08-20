import json

user_none_error = json.dumps(
    {'code':201,'data':{'context':'on','message':'用户不存在'}}
)
user_login_success = json.dumps(
    {'code':200,'data':{'context':'ok','message':'登录成功'}}
)
user_password_error = json.dumps(
    {'code':202,'data':{'context':'ok','message':'密码错误'}}
)
user_create_success = json.dumps(
    {'code':200,'data':{'context':'ok','message':'用户创建成功'}}
)