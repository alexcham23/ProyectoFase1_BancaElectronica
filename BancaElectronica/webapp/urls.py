from django.contrib import admin
from django.urls import  path
from webapp import views
urlpatterns=[
    path('',views.BancaPrincipal)
]