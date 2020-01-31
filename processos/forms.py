from django import forms


class AtivosForm(forms.Form):
    tipo_ativo = forms.CharField(label='Tipo Ativo', max_length=20)
    descricao_ativo = forms.CharField(label='Descrição Ativo', max_length=20)
    valor_ativo = forms.IntegerField(label='Valor do Ativo')
    data_ativo = forms.DateField(label='Data do Ativo')


class RentForm(forms.Form):
    mes = [
        ('JAN', 'Janeiro'),
        ('FEV', 'Fevereiro'),
        ('MAR', 'Março'),
        ('ABR', 'Abril'),
        ('MAI', 'Maio'),
        ('JUN', 'Junho'),
        ('JUL', 'Julho'),
        ('AGO', 'Agosto'),
        ('SET', 'Setembro'),
        ('OUT', 'Outubro'),
        ('NOV', 'Novembro'),
        ('DEZ', 'Dezembro'),
    ]
    investimento = forms.CharField(label='investimento', max_length=20)
    lucro_liquido = forms.CharField(label='lucro', max_length=20)


]
