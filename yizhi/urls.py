"""yizhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.conf.urls import url,include
import xadmin
from login.views import categories,ActiveUserView,loginView,CustomBackend,registerView,ForgetPwdView,ResetView
from login.views import loginView,user_login,ForgetPwdView,shoppingcart,presscenter,register_success,email_send,FAQ,feedback,feedbacksuccess,notice





urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name="index.html"),name="index"),
    url(r'^categories/$',categories,name="categories"),
    url(r'^shoppingcart/',shoppingcart,name="shoppingcart"),
    url('^login/$',loginView.as_view(),name="login"),
    url('^register/$',registerView.as_view(),name="register"),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    url(r'^register_success/$',register_success,name="register_success"),
    url(r'^email_send/$',email_send,name="email_send"),
    url(r'^FAQ/$',FAQ,name="FAQ"),
    url(r'^feedback/$',feedback.as_view(),name="feedback"),
    url(r'^news/',presscenter,name="news"),
    url(r'^feedback_success/',feedbacksuccess,name="feedbach_success"),
    url(r'^notice/',notice,name="notice"),


]
'''

    url(r'^xadmin/', include(xadmin.site.urls)),
   url(r'^message/$',message,name='message'),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url('^$',TemplateView.as_view(template_name="index.html"),name="index"),
    url('^login/$',loginView.as_view(),name="login"),
    url('^register/$',registerView.as_view(),name="register"),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    url(r'^liuyan/$',liuyan,name='liuyan'),
    url(r'^forget/$',ForgetPwdView.as_view(),name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name="reset_pwd"),
    url(r'^djread/$',djread,name="djread"),
    url(r'^user/$',user,name="user"),
    url(r'^djsearch/$',djsearch,name="djsearch"),
    url(r'^user_message/$',user_message,name="user_message"),
    url(r'^register_success/$',register_success,name="register_success"),
    url(r'^email_send/$',email_send,name="email_send"),
    url(r'^blog_proflie1/$',blog_proflie1,name="blog_proflie1"),
    url(r'^blog_proflie2/$',blog_proflie2,name="blog_proflie2"),
    url(r'^blog_proflie3/$',blog_proflie3,name="blog_proflie3"),
    url(r'^search_place1/$',search_place1,name="search_place1"),
    url(r'^search_place2/$',search_place2,name="search_place2"),
    url(r'^search_place3/$',search_place3,name="search_place3"),
 

]
'''