from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('signup/',views.signuppage,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('chat/',views.chatpage,name='chat'),
    path('logout/',views.LogoutPage,name='logout'),
    path('password-reset/',views.passresetpage,name='passreset'),
    path('getResponse',views.getResponse,name='getResponse'),
]