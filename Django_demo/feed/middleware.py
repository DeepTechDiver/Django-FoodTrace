from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from feed import models
import json

class Middleware(MiddlewareMixin):
    def process_request(self,request):
        print(request.path)
        if request.path != '/user/login' and request.path != '/user/create':
            token = request.COOKIES['token']
            user = models.user.objects.filter(token = token)
            if user.count() == 0:
                token_failed_result = json.dumps({'code':401,'data':'token失效'})
                return token_failed_result

