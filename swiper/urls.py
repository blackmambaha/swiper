"""swiper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user import api as user_api
from social import api as social_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'user/api/sumbit_phone',user_api.sumbit_phone),
    url(r'user/api/sumbit_vcode',user_api.sumbit_vcode),
    url(r'user/api/get_profile',user_api.get_profile),
    url(r'user/api/set_profile',user_api.set_profile),
    url(r'user/api/upload_icon',user_api.upload_icon),

    url(r'social/api/get_rcmd_user',social_api.get_rcmd_user),
    url(r'social/api/like',social_api.like),
    url(r'social/api/superlike',social_api.superlike),
    url(r'social/api/dislike',social_api.dislike),
    url(r'social/api/regret',social_api.regret),
    url(r'social/api/get_friends',social_api.get_friends),
    url(r'social/api/get_friend_info',social_api.get_friend_info),
]
