# 用户操作函数
from app.models import *
import re
from django.utils.timezone import timezone

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
    user = User(username = username, password_md5 = password_md5, email = email, phone = phone, balance = float("0.00"))
    user.save()
    return "%s" % user.id

def loginUser(username, password_md5):
    #成功返回账户id否则返回错误原因
    if username == "" or password_md5 == "":
        return "username or password is null"
    if len(User.objects.filter(username__iexact=username).values_list()) == 0:
        return "username not exists"
    user = User.objects.filter(username__iexact = username, password_md5__iexact = password_md5)
    if user:
        return "%s" % user.id
    else:
        return "password error"

def queryBalance(userid):
    #成功返回账户余额否则返回错误原因
    if userid == "":
        return "userid null"    
    user = User.objects.filter(id = userid)
    if user:
        return "%s" % user.first().balance
    else:
        return "userid error"

def queryDeadline(userid, appid):
    #成功返回过期时间则返回错误原因
    if userid == "" or appid == "":
        return "userid or appid null"    
    use = Use.objects.filter(userid__iexact = userid, appid__iexact = appid)
    if use:
        return "%s" % use.first().deadline
    else:
        return "user or appid not exists"

def addDalance(userid, value):
    #成功返回最新余额否则返回错误原因
    if userid == "" or value == "":
        return "userid or value null"   
    user = User.objects.filter(id = userid)
    if user:
        user_ = user.first().balance + float(value)
        user_.save()
        return "%s" % user_.balance
    else:
        return "userid not exists"

def useCard(userid, card_number, card_password):
    #成功返回最新余额否则返回错误原因
    if userid == "" or card_number == "" or card_password == "":
        return "userid or card null"   
    card = Card.objects.filter(number = card_number, password = card_password)
    if card:
        card_ = card.first()
        card_cost = card_.card_cost
        return_content = addDalance(userid=userid, value = card_cost)
        try:
            newbalance = float(return_content)
            card_.record = True
            card_.save()
            return newbalance
        except ValueError:
            return return_content
    else:
        return "card error"