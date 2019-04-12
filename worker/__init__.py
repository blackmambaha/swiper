#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：ben

# 任务队列
from celery import Celery
import os
from worker import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
celery_app = Celery('swiper')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()