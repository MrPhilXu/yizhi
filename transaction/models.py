#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.

class Transfer(models.Model):
    name = models.CharField(max_length=100,verbose_name=u"科技成果信息")
    image = models.ImageField(upload_to = "banner/%y/%m",verbose_name=u"图片",max_length = 100)
    type = models.CharField(max_length = 50,verbose_name=u"类型")
    subject = models.CharField(max_length = 50,verbose_name=u"所属学科")
    number = models.CharField(max_length=50,verbose_name=u"编号")
    price = models.IntegerField(default=0,verbose_name=u"价格")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"商品信息"
        verbose_name_plural = verbose_name