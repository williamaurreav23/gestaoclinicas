from django import forms


class LandForm(forms.Form):


nome_empresa = forms.CharField(
    label='nome_empresa', max_length=50,)
nome_contato = forms.CharField(
    label='nome-contato', max_length=50)
celular = forms.CharField(
    label='celular', max_length=10)
email = forms.EmailField(
    label='email', max_length=254)

interesse = [
    ('Consultoria', 'Consultoria'),
    ('Treinamento', 'Treinamento'),
    ('Marketing', 'Marketing'),
    ('Outros', 'Outros'),
]
