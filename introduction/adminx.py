# -*-coding:utf-8 -*-
#from django.contrib import admin

#Register your models here.
import xadmin
from .models import Banner,AboutPLat,MainTechnology,Goods
from xadmin import views

class BannerAdmin(object):
     list_display = ['title','image','url','index','add_time']
     search_fields = ['title','image','url','index']
     list_filter = ['title','image','url','index','add_time']

class AboutPLatAdmin(object):
    list_display = ['aboutplat','image','add_time']
    search_fields = ['aboutplat','image']
    list_filter = ['aboutplat','image','add_time'] 

class MainTechnologyAdmin(object):
    list_display = ['technology','image','add_time']
    search_fields = ['technology','image']
    list_filter = ['technology','image','add_time']

class GoodsAdmin(object):
    list_display = ['new_goods_url','recommend_url','hot_goods_url','add_time']
    search_fields = ['new_goods_url','recommend_url','hot_goods_url']
    list_filter = ['new_goods_url','recommend_url','hot_goods_url','add_time']    



xadmin.site.register(Banner,BannerAdmin)  
xadmin.site.register(AboutPLat,AboutPLatAdmin) 
xadmin.site.register(MainTechnology,MainTechnologyAdmin) 
xadmin.site.register( Goods,GoodsAdmin)  
    


