from django.contrib import admin
from django.urls import  path
from webapp import views
urlpatterns=[
    path('',views.BancaPrincipal),
    path('EstadoCuenta/',views.EstadoCuenta,name='EstadoCuenta'),
]