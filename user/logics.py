#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：ben

import os
from lib.qiniu_cloud import upload_to_qiniu
from swiper import settings
from urllib.parse import urljoin
from swiper import config
from worker import celery_app


def upload_icon_to_server(uid,icon):
    file_name = 'icon-%s' % uid + os.path.splitext(icon.name)[1]
    save_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, file_name)


    with open(save_path, 'wb') as fp:
        for chunk in icon.chunks():
            fp.write(chunk)

    return file_name, save_path


@celery_app.task
def upload_icon(user,icon):
    filename, saved_path = upload_icon_to_server(user.id, icon)
    upload_to_qiniu(filename, saved_path)
    icon_url = urljoin(config.QINIU_BUCKET_URL, filename)
    # 前端可以取到这个icon_url把头像取出来
    user.icon = icon_url
    user.save()