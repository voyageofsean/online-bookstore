from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('information/<str:isbn>', views.information, name='information'),
    path('display/', views.display, name='display'),
]
