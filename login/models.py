# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
	nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
	birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
	gender = models.CharField(verbose_name=u"性别",max_length=50,choices=(("male",u"男"),("female",u"女")),default="female")
	address = models.CharField(verbose_name=u"地址",max_length=100,default="")
	mobile = models.CharField(verbose_name=u"手机号码",max_length=11,null=True,blank=True)
	image = models.ImageField(verbose_name=u"头像",upload_to="media/image/%Y/%m",default="media/image/man.jpeg",max_length=100)
	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name
	def  __unicode__(self):
		return self.username

class EmailVerifyRecord(models.Model):
	code = models.CharField(max_length=20,verbose_name=u"验证码")
	email = models.EmailField(max_length=50,verbose_name=u"邮箱")
	send_type = models.CharField(verbose_name=u"验证码",choices=(("register",u"注册"),("forget",u"找回密码")),max_length=10)
	send_time = models.DateTimeField(verbose_name=u"验证码",default=datetime.now)

	class Meta:
		verbose_name = u"邮箱验证码"
		verbose_name_plural = verbose_name
	def __unicode__(self):
		return '{0}({1})'.format(self.code,self.email)


class feedback(models.Model):
    jianyi = models.CharField(max_length=200,verbose_name=u"反馈")
    xingming = models.CharField(max_length=10,verbose_name=u"姓名")
    emailfeedback = models.EmailField(max_length=50,verbose_name=u"邮箱")
    class Meta:
	    verbose_name = u"用户反馈"
	    verbose_name_plural = verbose_name
    def  __unicode__(self):
    	return self.username



