from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def rotatividade(admissoes, demissoes, colaboadores):
    numerador = (admissoes + demissoes) / 2
    racio = numerador / colaboadores
    taxa = racio * 100
    print("o valor de rotatividade foi de :", taxa, "%")


class PessoasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pessoas/pessoas.html', {})

def get_data(request, *args, **kwargs);
    data= {
        "salario":100,
        "beneficios": 50,
    }
    return JsonResponse(data) #http response