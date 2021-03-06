# coding:utf-8
from django.conf.urls import url,include
from df_user import views

urlpatterns = [
    url(r'^register/$',views.register,name='register'), # 注册界面
    url(r'^check_uname/',views.check_uname),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login/$',views.login), #　登录界面
    # url(r'^login_handle/$',views.login_handle),
    # url(r'^login_handle_2/$', views.login_handle_2),
    url(r'^login_handle_3/$', views.login_handle_3),

    url(r'^user_center_info/$',views.user_center_info),  # 用户中心界面(默认为个人信息界面)
    url(r'^user_center_order/(\d*)',views.user_center_order),   # 用户中心-全部订单
    url(r'^user_center_site/$',views.user_center_site),   # 用户中心-收货地址(打开链接+处理提交的数据)

    url(r'^login_out/$',views.login_out),
]

