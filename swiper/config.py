#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：ben

# 配置文件
# 写一个路由
YZX_SMS_URL = 'https://open.ucpaas.com/ol/sms/sendsms'
# YZX_SMS_URL = 'https://open.ucpaas.com/ol/sms/{function}'


YZX_SMS_PARAMS = {
    "sid": "b0ec7dcb7d1502401290551656b63a09",
    "token": "816260cceb0fdeb6394767235044d7bd",
    "appid": "a277aca9950d4809aa27d72d4abae888",
    "templateid": "453182",
    "param": None,
    "mobile": None,
}

# 需要填写你的 Access Key 和 Secret Key
QINIU_ACCESS_KEY = 'Access_Key'
QINIU_SECRET_KEY = 'Secret_Key'
# 要上传的空间
QINIU_BUCKET_NAME = 'swipe'

QINIU_BUCKET_URL = 'http://'

# 反悔次数
REGRET_TIMES = 3