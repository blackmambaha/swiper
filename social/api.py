from django.shortcuts import render

from lib.http_sms import render_json
from social import logics
from user.models import User
from common import errors


def get_rcmd_user(request):
    # 取出用户
    user = request.user
    users = logics.get_rcmd_users(user)
    # 推荐用户列表
    users_list = [user.to_string() for user in users]

    return render_json(users_list)


def like(request):
    # 判断是否是post请求
    if not request.method == 'POST':
        return render_json('request method error', errors.REQUEST_ERROR)

    sid = int(request.POST.get('sid'))
    matched = logics.like(request.user,sid)

    return render_json({'matched':matched})


def superlike(request):
    # 判断是否是post请求
    if not request.method == 'POST':
        return render_json('request method error', errors.REQUEST_ERROR)

    sid = int(request.POST.get('sid'))
    matched = logics.superlike(request.user, sid)

    return render_json({'matched': matched})


def dislike(request):
    # 判断是否是post请求
    if not request.method == 'POST':
        return render_json('request method error', errors.REQUEST_ERROR)

    sid = int(request.POST.get('sid'))
    logics.dislike(request.user,sid=sid)

    return render_json(None)


def regret(request):
    breaked = logics.regret(request.user)
    return render_json({'regret':breaked})


def get_friends(request):
    pass


def get_friend_info(request):
    pass

