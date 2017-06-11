from django import forms
from django.contrib.auth.models import User
from core.models import *
from django.forms import ModelForm


class Login(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')


class NewUser(forms.Form):
    tipo = (
        ('RH', 'RH'),
        ('JO', 'Jornalista'),
        ('FO', 'Fotografo'),
        ('ED', 'Editor'),
    )
    nome = forms.CharField(label="Nome")
    login = forms.CharField(label="Nome de Usuario")
    senha = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    confirma_senha = forms.CharField(widget=forms.PasswordInput(), label="Confirmacao")
    email = forms.EmailField(label='Email')
    tipo_usuario = forms.ChoiceField(label="Tipo de Usuario", choices=tipo)

    def clean_login(self):
        login = self.cleaned_data['login']
        try:
            User.objects.get(username=self.cleaned_data['login'])
        except User.DoesNotExist:
            return login
        raise forms.ValidationError('Login ja existe')

    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError('Login ja existe')

    def clean(self):
        if self.cleaned_data['senha'] != self.cleaned_data['confirma_senha']:
            raise forms.ValidationError('Senha e Confirmaçao nao correspondem')
        else:
            return self.cleaned_data


class CadernoForm(ModelForm):
    class Meta:
        model = Caderno
        fields = ['nome', 'descricao']

    def clean(self):
        if Caderno.objects.filter(nome=self.cleaned_data['nome']).exists():
            raise forms.ValidationError('Caderno ja existe')
        else:
            return self.cleaned_data

class CadernoFormEdit(ModelForm):
    class Meta:
        model = Caderno
        fields = ['nome', 'descricao']

    def clean(self):
        return self.cleaned_data

