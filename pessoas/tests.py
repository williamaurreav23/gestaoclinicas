from django.test import TestCase

# Create your tests here.
# Carlos Pedro Gonçalves
# Instituto Superior de Ciências Sociais e Políticas (ISCSP) - Universidade de Lisboa
# E-mail: cgoncalves@iscsp.ulisboa.pt
#
# Aulas de programação aplicada à tomada de decisão em Gestão de Recursos Humanos:
# Unidade Curricular de Estatística para a Gestão II
#
# Exercício de aplicação do Python à Gestão de Recursos Humanos: caso de atribuição de prémios a vendedores
# 13-05-2015


class Vendedor:
    def __init__(self, codigo, nome, vendas):
        self.codigo = codigo
        self.nome = nome
        self.vendas = vendas

    def avaliaVendedor(self, mediaVendas, proporcao):
        if self.vendas > mediaVendas:
            premio = proporcao * self.vendas
            print
            self.codigo, self.nome, 'recebe prémio de', premio, 'euros'


listaVendedores = []

listaVendedores.append(Vendedor('V01', 'Ambrósio Severino Pais', 500000))
listaVendedores.append(Vendedor('V02', 'Ana Leopolda Leopardo', 650000))
listaVendedores.append(Vendedor('V03', 'Ana Reis Corrais', 320000))
listaVendedores.append(Vendedor('V04', 'Blimunda Refrescada Sais', 450000))
listaVendedores.append(Vendedor('V05', 'Dário Vidigais do Finigal', 350000))
listaVendedores.append(Vendedor('V06', 'Eduarda Susana Cimeira', 300000))
listaVendedores.append(Vendedor('V07', 'Helena Correia Zifulmática', 360000))
listaVendedores.append(Vendedor('V08', 'João Sumido Santeiro', 470000))
listaVendedores.append(Vendedor('V05', 'Jorge Santos Reis Tomar', 420000))
listaVendedores.append(Vendedor('V05', 'Jorge Pais dos Reis', 430000))

listaVendas = []

for trabalhador in listaVendedores:
    listaVendas.append(trabalhador.vendas)

somaVendas = sum(listaVendas)
mediaVendas = somaVendas / len(listaVendas)

for trabalhador in listaVendedores:
    trabalhador.avaliaVendedor(mediaVendas, 0.005)