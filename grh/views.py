from django.shortcuts import render

# Create your views here.

def rotatividade(admissoes, demissoes, colaboadores):
    numerador = (admissoes + demissoes) / 2
    racio = numerador / colaboadores
    taxa = racio * 100
    print("o valor de rotatividade foi de :", taxa, "%")


def grh(request):
    return render(request, 'funcionarios.html')

def desempenho(request):
    return render(request, 'desempenho.html')