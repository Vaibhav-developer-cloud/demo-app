
from django.urls import path,include
from . import views
from .views import BookListView,BookDetailView
from django.contrib.auth import views as auth_view

urlpatterns = [               #polls.urls and appname,catalog urls in variable is
                                # #carefully cheak becase not same through the error import circular
 path('',views.index,name="indexing"),
 path('Books/',BookListView.as_view(), name="Books"),
 path('Books/<int:pk>', BookDetailView.as_view(), name="Books"),
 path('setcookies/',views.setting_cookie,name="set cookies"),
 path('getcookies/',views.getting_cookie,name="get cookies"),
 path('delete_cookies/', views.delete_cookie, name="delete cookies"),
 path('user/',views.user_creation,name='user creation'),
 path('login/',auth_view.LoginView.as_view(),name='login'),
 path('password_change/',auth_view.PasswordChangeView.as_view(),name="password_change"),
 path('password_change/', auth_view.PasswordChangeView.as_view(), name="password_change"),
 path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(), name="password_change_done"),
 path('password_reset/', auth_view.PasswordResetView.as_view(), name="password_reset"),
 path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
 path('password_reset_confirm',auth_view.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
 path('password_reset_complete', auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
 path('input_view',views.input_view, name="input_view"),
 path('register', views.employee_register, name="register")

]


# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#
#     path('hello/',views.hello,name="hello"),
#
#     path('calculate/', views.calculate,name="cal"),
#
#     path('index/',views.index,name="indexing page")
# ]