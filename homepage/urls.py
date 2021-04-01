from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('shorten',views.shorten,name='shorten'),
    path('<str:token>',views.urlRedirect,name='urlRedirect')
]