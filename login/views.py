# -*-coding:utf-8 -*-
from django.contrib.auth import authenticate, login
# Create your views here.
#
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic.base import View

from utils.email_send import send_register_email
from .forms import loginForm,registerForm,forgetForm
from login.models import UserProfile,EmailVerifyRecord


'''def index(request):
    return render(request,"index.html")'''

def categories(request):
	return render(request,"categories.html")

class CustomBackend(ModelBackend):
	def authenticate(self,username=None,password=None,**kwargs):
		try:
			user=UserProfile.objects.get(username=username)
			if user.check_password(password):
				return user
		except Exception as e:
			return None


class ActiveUserView(View):
	def get(self,request,active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email
				user = UserProfile.objects.get(email=email)
				user.is_active = True
				user.save()
		else:
			return render(request,"404.html")#lianjie shi xiao
		return render(request,"login.html")

class registerView(View):

	def get(self,request):
		register_form = registerForm()
		return render(request,"register.html",{'register_form':register_form})

	def post(self,request):
		register_form = registerForm(request.POST)
		if register_form.is_valid():
			user_name = request.POST.get("email","")
			if UserProfile.objects.filter(email=user_name):
				return render(request,"register.html",{"register_form":register_form,"msg":"用户已经存在！"})

			pass_word = request.POST.get("password","")
			user_profile = UserProfile()
			user_profile.username = user_name
			user_profile.email   = user_name
			user_profile.password = make_password(pass_word)
			user_profile.save()
			
			send_register_email(user_name,"register")
			return render(request,"email_send.html")
		else:

			return render(request,"register.html",{"register_form":register_form})



class loginView(View):
	def get(self,request):
		return render(request,"login.html",{})
	def post(self,request):
		login_form = loginForm(request.POST)
		if login_form.is_valid():
			user_name = request.POST.get("username","")
			pass_word = request.POST.get("password","")
			user = authenticate(username=user_name,password=pass_word)
			if user is not None:
				if user.is_active:
					login(request,user)
					return render(request,"index.html")
				else:
					return render(request, "login.html", {"msg": "用户名或密码错误!"})
			else:
				return render(request,"login.html",{"msg":"用户名或密码错误!"})

		else:
			return render(request,"login.html",{"login_form":login_form})


def user_login(request):


	if request.method == "POST":
		user_name = request.POST.get("username","")
		pass_word = request.POST.get("password","")
		user = authenticate(username=user_name,password=pass_word)
		if user is not None:
			login(request,user)
			return render(request,"index.html")

		else:
			return render(request,"login.html",{"msg":"用户名或密码错误!"})


	elif request.method == "GET":
		return render(request,"login.html",{})

class ForgetPwdView(View):
	def get(self,request):
		forget_form = forgetForm()
		return render(request,"forgetpwd.html",{"forget_form":forget_form})

	def post(self,request):
		forget_form = forgetForm(request.POST)
		if forget_form.is_valid():
			email = request.POST.get("email","")
			send_register_email(email,"forget")
			return render(request,"send success.html")

		else:
			return render(request,"forgetpwd.html",{"forget_form":forget_form})


class ResetView(View):
	def get(self,request,active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email
				return render(request,"password_reset.html",{"email":email})
		else:
			return render(request,"404.html")#error
		return render(request,"login.html")


def shoppingcart(request):
	return render(request,"shoppingcart.html")

































def djsearch(request):
	return render(request,"djsearch.html")



def user(request):
	return render(request,"user.html")

def user_message(request):
	return render(request,"user_message.html")
def email_send(request):
	return render(request,"email_send.html")
def register_success(request):
	return render(request,"register_success.html")


def blog_proflie1(request):
	return render(request,"blog_proflie1.html")

def blog_proflie2(request):
	return render(request,"blog_proflie2.html")

def blog_proflie3(request):
	return render(request,"blog_proflie3.html")

def search_place1(request):
	return render(request,"search_place1.html")

def search_place2(request):
	return render(request,"search_place2.html")

def search_place3(request):
	return render(request,"search_place3.html")
