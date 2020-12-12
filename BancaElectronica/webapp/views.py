from django.shortcuts import render

# Create your views here.
def BancaPrincipal(request):
    return render(request,'Cuenta.html')