# -*-coding:utf-8 -*-
from login.models import EmailVerifyRecord
from django.core.mail import send_mail
from yizhi.settings import EMAIL_FROM
from random import Random

def send_register_email(email,send_type="register"):
	email_record = EmailVerifyRecord()
	code = random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()


	email_title = ""
	email_body = ""

	if send_type == "register":
		email_titlse = "独景网邮箱激活"
		email_body = "感谢您在我站注册了新帐号。请点击链接激活您的帐号。http://127.0.0.1:8000/active/{0}".format(code)
		send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
		if send_status:
			pass
	elif send_type == "forget":
		email_title = "独景网密码重置"
		email_body = "请点击以下链接重置密码。http://127.0.0.1:8000/reset/{0}".format(code)
		send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
		if send_status:
			pass


def random_str(randomlength=8):
	str=''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str+=chars[random.randint(0,length)]
	return str

