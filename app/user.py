# 用户操作函数
from app.models import *
import re
from datetime import datetime

def regUser(username, password_md5, email, phone=""):
    #成功返回数据库数值Id否则返回错误原因
    if username == "" or password_md5 == "" or email == "":
        return "username or password or email is null"
    if len(User.objects.filter(username__iexact=username).values_list()) != 0:
        return "username exists"
    email_p = re.compile(r'[^\._][\w\._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')
    if not(email_p.match(str)):
        return "email error"
    if phone !="":
        if len(phone) != 14:
            return "phone len error"
    user = User(username = username, password_md5 = password_md5, email = email, phone = phone)
    user.save()
    return user.id

def loginUser(username, password_md5):
    #成功返回账户余额否则返回错误原因
    if username == "" or password_md5 == "":
        return "username or password is null"
    if len(User.objects.filter(username__iexact=username).values_list()) == 0:
        return "username not exists"
    user = User.objects.filter(username__iexact = username, password_md5__iexact = password_md5)
    if user:
        user.first().updatetime = datetime.strftime()
        return user.balance
    else:
        return "password error"

def queryBalance(username):
    if username == "":
        return "username null"    
    user = User.objects.filter(username__iexact = username).first()
    if user:
        return user.balance
    else:
        return "password error"