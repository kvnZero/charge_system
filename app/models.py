from django.db import models

class User(models.Model):
    username = models.CharField(max_length=256)
    password_md5 = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256, null=True)
    balance = models.IntegerField(default=0)
    
class App(models.Model):
    appname = models.CharField(max_length=256)
    version = models.CharField(max_length=256)
    downloadurl = models.CharField(max_length=256)

class Use(models.Model):
    userid = models.CharField(max_length=256)
    appid = models.CharField(max_length=256)
    usekey = models.CharField(max_length=256)
    deadline = models.DateTimeField()

class Card(models.Model):
    number = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    cost = models.IntegerField()
    record = models.BooleanField()

class Buy(models.Model):
    wechatid = models.CharField(max_length=256)
    number = models.IntegerField()
    total = models.CharField(max_length=256)

class Order(models.Model):
    wechatid = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    money = models.CharField(max_length=256)
    time = models.DateTimeField()
    record = models.BooleanField()