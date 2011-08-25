#coding:utf-8
from django.db import models

class Inscricoes(models.Model):
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    id_inscrito = models.AutoField('ID Inscrito', primary_key = True)
    nome = models.CharField('Nome', max_length = 50)
    cpf = models.CharField('CPF', max_length = 14)
    
    def __unicode__(self):
        return self.nome
        
class Minicursos(models.Model):
    class Meta:
        verbose_name = 'Mini-Curso'
        verbose_name_plural = 'Mini-Cursos'
    id_minicurso = models.AutoField('ID Minicurso', primary_key = True)
    titulo = models.CharField('Título', max_length=100)
    vagas = models.IntegerField('Total de vagas', max_length=2)
    inscritos = models.IntegerField('Inscritos', max_length=2)
