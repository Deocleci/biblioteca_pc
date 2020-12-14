from django.db import models
from user.models import CustomUser

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    codigo = models.CharField(max_length=16)
    editora = models.CharField(max_length=200)
    emprestado = models.BooleanField("Emprestado?", blank=True, null=True,  default=False)
    user = models.ForeignKey(CustomUser, verbose_name='Usuário', blank=True, null=True, editable=True, on_delete=models.CASCADE)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo',]


    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.criado_em}/{self.atualizado_em})"