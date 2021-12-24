from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def foro(request):
    return render(request, 'foro.html')

def Registrarme(request):
	return render(request, 'Registrarme.html')
#class Registrarme(CreateView):
def recuperarcontraseña(request):
	return render(request, 'recuperarcontraseña.html')

def QueeselODS(request):
    return render(request, 'QueeselODS.html')

def ODS1(request):
    return render(request, 'pagians del ODS\ODS1.html')

def ODS2(request):
    return render(request, 'pagians del ODS\ODS2.html')

def ODS3(request):
    return render(request, 'pagians del ODS\ODS3.html')

def ODS4(request):
    return render(request, 'pagians del ODS\ODS4.html')

def ODS5(request):
    return render(request, 'pagians del ODS\ODS5.html')

def ODS6(request):
    return render(request, 'pagians del ODS\ODS6.html')

def ODS7(request):
    return render(request, 'pagians del ODS\ODS7.html')

def ODS8(request):
    return render(request, 'pagians del ODS\ODS8.html')

def ODS9(request):
    return render(request, 'pagians del ODS\ODS9.html')

def ODS10(request):
    return render(request, 'pagians del ODS\ODS10.html')

def ODS11(request):
    return render(request, 'pagians del ODS\ODS11.html')

def ODS12(request):
    return render(request, 'pagians del ODS\ODS12.html')

def ODS13(request):
    return render(request, 'pagians del ODS\ODS13.html')

def ODS14(request):
    return render(request, 'pagians del ODS\ODS14.html')

def ODS15(request):
    return render(request, 'pagians del ODS\ODS15.html')

def ODS16(request):
    return render(request, 'pagians del ODS\ODS16.html')

def ODS17(request):
    return render(request, 'pagians del ODS\ODS17.html')
