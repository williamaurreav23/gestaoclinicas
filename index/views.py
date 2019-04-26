from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def gestao(request):
    return render(request, 'gestao.html')

def top(request):
    return render(request, 'top.html')

def planejamento(request):
    return render(request, 'planejamento.html')

def marketing(request):
    return render(request, 'marketing.html')

def design(request):
    return render(request, 'design.html')

def data(request):
    return render(request, 'data.html')
    