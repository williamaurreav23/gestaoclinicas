from django import forms


class ComentarioForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    comentario = forms.CharField(widget=forms.Textarea)
    url = forms.URLField(label='url', max_length=100)