#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：ben

from django.utils.deprecation import MiddlewareMixin
from user.models import User
from lib.http_sms import render_json
from common import errors


# 验证是否登录的中间件
class AuthMiddleware(MiddlewareMixin):
    URL_WHITE_LIST = [
        '/user/api/sumbit_phone',
        '/user/api/sumbit_vcode',
    ]

    def process_request(self,request):
        if request.path in self.URL_WHITE_LIST:
            return
        # 注意，uid保存在session中
        uid = request.session.get('uid')
        if not uid:
            return render_json('user not login',errors.USER_NOT_LOGIN)
        try:
            # 根据uid取到用户
            user = User.objects.get(id=uid)
            request.user = user
        except User.DoesNotExist:
            return render_json('no this user',errors.NO_THIS_USER)
