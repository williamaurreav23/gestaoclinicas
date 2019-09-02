from django import forms


class bdclientes(forms.Form):
    class meta:
        fields = ['id_cliente','nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
        # widget = {
        #     'nome' : forms.Textarea(attrs={'size': '40'}),
        #     'sobrenome' : forms.TextInput(attrs={'class': 'input is-danger'}),
        #     'cnpj' : forms.TextInput(attrs={'class': 'input is-danger'}),
        #     'celular' : forms.TextInput(attrs={'class': 'input is-danger'}),
        #     'email' : forms.TextInput(attrs={'class': 'input is-danger'})

        # }

#
#        fields = ['id_cliente','nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
#        widgets={'nome': Textarea(attrs={'class' : 'form-control'})})
#
# class Media:
#         css = {
#             'all': ('bulma.css',)
#         }
