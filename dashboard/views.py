from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def listclientes(request):
    return render(request, 'listclientes.html')
