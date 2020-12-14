from django.contrib import admin
from django.urls import  path
from webapp import views
urlpatterns=[
    path('',views.BancaPrincipal),
    path('EstadoCuenta/',views.EstadoCuenta,name='EstadoCuenta'),
    path('PlanillaProveedor/',views.PlanillaProveedor,name='PlanillaProveedor'),
    path('Transferencia-a-Tercero/',views.Tercero,name='tercero')
]