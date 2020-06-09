from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login),
    path('register/',views.register),
    path('search/',views.search),
    #不知道为什么没匹配成 有个常用匹配 https://www.jianshu.com/p/257fafc217df
    path(r'^bookInformation/(?P<isbn>[-\w]+)/$',views.bookInformation),
    path('showBook/',views.showBook),
]