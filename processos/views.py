from django.shortcuts import render

# Create your views here.


class AtivoCreate(CreateView):
    model = Ativos
    fields = ['id_ativo', 'tipo_ativo',
              'descricao_ativo', 'valor_ativo', 'data_ativo']


class PassivoCreate(CreateView):
    model = Passivos
    fields = ['id_passivo', 'tipo_passivo',
              'descricao_passivo', 'valor_passivo', 'data_passivo']


class AtivosView(DetailView):
    model = Ativos
    template_name = 'dashboard.html'
    query_pk_and_slug = 'id_ativo=1'


class RentView(CreateView):
    model = Rentabilidade
    fields = ['data_inicio', 'data_fim', 'investimento',
              'lucro_liquido', 'rentabilidade']
    success_url = reverse_lazy('dashboard')


class RentabilidadeDetail(DetailView):
    model = Rentabilidade
    template_name = 'dashboard.html'


class InvestimentoDetail(DetailView):
    model = Rentabilidade
    template_name = 'dashboard.html'
    query_pk_and_slug = 'id=1'
