#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length = 100,verbose_name = u"标题")
    image = models.ImageField(upload_to = "banner/%y/%m",verbose_name=u"轮播图",max_length = 100)
    url = models.URLField(max_length = 200,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

class AboutPLat(models.Model):
    aboutplat = models.TextField(verbose_name=u"关于平台")
    image = models.ImageField(upload_to = "plat/%y/%m",verbose_name=u"图片",max_length = 100)
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")        

    class Meta:
        verbose_name=u"关于平台"  
        verbose_name_plural = verbose_name

class MainTechnology(models.Model):
    technology = models.TextField(verbose_name=u"科技介紹",default="")
    image = models.ImageField(upload_to = "technologyes/%y/%m",verbose_name=u"图片",max_length = 100,default="")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")        

    class Meta:
        verbose_name=u"科技介紹"
        verbose_name_plural = verbose_name


class Goods(models.Model):
    new_goods_url = models.URLField(max_length = 200,verbose_name=u"最新成果") 
    recommend_url = models.URLField(max_length = 200,verbose_name=u"精品推荐")
    hot_goods_url = models.URLField(max_length = 200,verbose_name=u"最熱商品") 
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")        


    class Meta:
        verbose_name=u"浏览商品"
        verbose_name_plural = verbose_name     


