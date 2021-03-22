from django.contrib import admin
from django.urls import path
from . import views

app_name = 'investment'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('processsignup/', views.processsignup, name='processsignup'),
    path('signupsuccess/<sign_up_data>',views.signupsuccess,name='signupsuccess'),

]

