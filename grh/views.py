from django.shortcuts import render

# Create your views here.

def rotatividade(admissoes, demissoes, colaboadores):
    numerador = (admissoes + demissoes) / 2
    racio = numerador / colaboadores
    taxa = racio * 100
    print("o valor de rotatividade foi de :", taxa, "%")


def pessoas(request):
    return render(request, 'pessoas/pessoas.html')