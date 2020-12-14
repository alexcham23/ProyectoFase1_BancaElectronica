from django.shortcuts import render

# Create your views here.
def BancaPrincipal(request):
    return render(request,'Cuenta.html')
    
def EstadoCuenta(request):
    return render(request,'Estado.html')

def PlanillaProveedor(request):
    return render(request,'Planpro.html')

def Tercero(request):
    return render(request,'Terceros.html')

    