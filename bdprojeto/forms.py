from django import forms


class ClienteForms(forms.Form):

        nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        cnpj = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        email = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))

# class Media:
#         css = {
#             'all': ('bulma.css',)
#         }
