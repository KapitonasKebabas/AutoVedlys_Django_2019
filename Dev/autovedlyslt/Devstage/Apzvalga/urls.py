from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.logInHtml, name="logInHtml"),
    path('papildymaiHtml', views.papildymaHtml, name="papildymaHtml"),
    path('apzvalgaHtml', views.apzvalgaHtml, name="apzvalgaHtml"),
    path('registerHtml', views.registerHtml, name="registerHtml"),
    path('logIn', views.logIn, name="logIn"),
    path('register', views.register, name="register"),
    path('logOut', views.logOut, name="logOut"),
    path('sustojimasAddHtml', views.sustojimasAddHtml, name="sustojimasAddHtml"),
    path('sustojimasAdd', views.sustojimasAdd, name="sustojimasAdd")
    
]