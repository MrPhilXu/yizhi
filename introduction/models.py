#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length = 100,verbose_name = u"標題")
    image = models.ImageField(upload_to = "banner/%y/%m",verbose_name=u"輪播圖",max_length = 100)
    url = models.URLField(max_length = 200,verbose_name=u"訪問地址")
    index = models.IntegerField(default=100,verbose_name=u"順序")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加時間")

    class Meta:
        verbose_name = u"輪播圖"
        verbose_name_plural = verbose_name

class AboutPLat(models.Model):
    aboutplat = models.TextField(verbose_name=u"關於平臺")
    image = models.ImageField(upload_to = "banner/%y/%m",verbose_name=u"圖片",max_length = 100)
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加時間")        

    class Meta:
        verbose_name=u"關於平臺"  
        verbose_name_plural = verbose_name

class MainTechnology(models.Model):
    pass


