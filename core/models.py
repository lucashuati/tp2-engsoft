from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    tipo_usuario = models.CharField(max_length=2)
    pk_user = models.IntegerField()
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_user(self):
        if self.tipo == 'RH':
            return RH.objects.get(pk=self.pk)
        if self.tipo == 'JO':
            return Jornalista.objects.get(pk=self.pk)
        if self.tipo == 'FO':
            return Fotografo.objects.get(pk=self.pk)
        if self.tipo == 'ED':
            return Editor.objects.get(pk=self.pk)


class RH(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)


class Jornalista(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)


class Fotografo(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)


class Editor(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=True, null=True)
