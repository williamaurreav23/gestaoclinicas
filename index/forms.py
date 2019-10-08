
from django import forms


class ClienteForms(forms.Form):

        nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
        sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
        cnpj = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
        celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
        email = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))