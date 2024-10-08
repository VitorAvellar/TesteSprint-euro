from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User


class Setores(models.Model):
    nome_setor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_setor

class Modulos(models.Model):
    nome_modulo = models.CharField(max_length=255)
    video = models.ForeignKey('AcervoVideos', on_delete=models.SET_NULL, null=True, blank=True)  # Referenciar com string

    def __str__(self):
        return self.nome_modulo

class Clientes(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cliente", null=True)
    nome = models.CharField(max_length=255)
    setor = models.ForeignKey(Setores, on_delete=models.SET_NULL, null=True)
    data_de_nascimento = models.DateField(null=True)
    data_inscricao = models.DateTimeField(default=timezone.now)
    email = models.EmailField()

class Treinamentos(models.Model):
    nome_treinamento = models.CharField(max_length=255)
    setor = models.ForeignKey(Setores, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nome_treinamento
    
class AcervoVideos(models.Model):
    nome_video = models.CharField(max_length=255)
    descricao = models.TextField()
    url_video = models.URLField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    
    setor = models.ForeignKey(Setores, on_delete=models.SET_NULL, null=True)  # Relaciona com o setor

    def __str__(self):
        return self.nome_video

class TipoPergunta(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Pergunta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_pergunta = models.ForeignKey('TipoPergunta', on_delete=models.SET_NULL, null=True)
    texto_pergunta = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto_pergunta

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    texto_resposta = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Torna opcional
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto_resposta
    
class Material(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='core/')
    modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title


class Exercicio(models.Model):
    pergunta = models.CharField(max_length=255)
    alternativa_a = models.CharField(max_length=255)
    alternativa_b = models.CharField(max_length=255)
    alternativa_c = models.CharField(max_length=255)
    alternativa_d = models.CharField(max_length=255)
    alternativa_e = models.CharField(max_length=255, blank=True, null=True)
    resposta_correta = models.CharField(max_length=1)
    treinamento = models.ForeignKey(Treinamentos, on_delete=models.SET_NULL, null=True)
    modulo = models.ForeignKey(Modulos, on_delete=models.SET_NULL, null=True)
