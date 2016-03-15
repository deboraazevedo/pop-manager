# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class AuditModel(models.Model):

    created_at = models.DateTimeField(
        u'Criado em',
        auto_now=True
    )

    edited_at = models.DateTimeField(
        u'Editado em',
        auto_now=True
    )

    class Meta:
        abstract = True

class Management(models.Model):
    name = models.CharField(
        u'Gerência',
        max_length=100,
        help_text=u'Insira uma gerência *'
    )
    description = models.TextField(
        u'Descrição',
        help_text=u'Insira uma descrição *'
    )

    class Meta:
        verbose_name=u'Gerência'
        verbose_name_plural=u'Gerências'
        ordering = ['-id']


    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField(
        u'Diretoria',
        max_length=100,
        help_text=u'Insira uma diretoria *'
    )
    description = models.TextField(
        u'Descrição',
        help_text=u'Insira uma descrição *'
    )
    management = models.ManyToManyField(
        Management,
        verbose_name=u'Gerêcias',
        help_text=u'Selecione as gerências *'
    )

    class Meta:
        verbose_name=u'Diretoria'
        verbose_name_plural=u'Diretorias'
        ordering = ['-id']

    def __str__(self):
        return self.name


class People(AbstractUser):
    office = models.CharField(
        u'Cargo',
        max_length=100,
        unique=True,
        help_text=u'Insira o cargo *'
    )
    direction = models.ManyToManyField(
        Direction,
        verbose_name=u'Diretorias',
        help_text=u'Informe as diretorias *'
    )


    class Meta:
        verbose_name=u'Pessoa'
        verbose_name_plural=u'Pessoas'
        ordering = ['-id']

    def __str__(self):
        return self.username



class Activity(models.Model):

    EASY = u'Baixa'
    NORMAL = u'Normal'
    HARD = u'Alta'
    OPTIONS = (
        (EASY, u'Baixa'),
        (NORMAL, u'Normal'),
        (HARD, u'Alta'),
    )

    name = models.CharField(
        u'Nome',
        max_length=100,
        help_text=u'Insira o nome completo *'
    )

    description = models.TextField(
        u'Descrição',
        help_text=u'Insira a descrição da atividade *'
    )

    management = models.ManyToManyField(
        Management,
        verbose_name=u'Gerêcias',
        help_text=u'Selecione as gerências *'
    )

    priority = models.CharField(
        u'Prioridade',
        choices=OPTIONS,
        default=EASY,
        max_length=100,
        help_text=u'Informe uma prioridade *'
    )

    status = models.BooleanField(
        u'Finalizado',
        help_text=u'Marque apenas se a atividade estiver finalizada'
    )

    class Meta:
        verbose_name=u'Atividade'
        verbose_name_plural=u'Atividades'
        ordering = ['-id']

    def __str__(self):
        return self.name



class Task(models.Model):

    EASY = 'Baixa'
    NORMAL = 'Normal'
    HARD = 'Alta'
    OPTIONS = (
        (EASY, 'Baixa'),
        (NORMAL, 'Normal'),
        (HARD, 'Alta'),
    )

    name = models.CharField(
        u'Título',
        max_length=100,
        help_text=u'Insira um nome da tarefa *'
    )


    start_date = models.DateTimeField(
        u'Data de inicio',
        help_text=u'Insira a data de inicio *'
    )

    conclusion_date = models.DateTimeField(
        u'Data de conclusão',
        help_text=u'Insira a data de conclusão *'
    )

    people = models.ForeignKey(
        People,
        verbose_name=u'Responsável',
        help_text=u'Selecione uma pessoa para essa tarefa *'
    )

    description = models.TextField(
        u'Descrição',
        help_text=u'Insira uma descrição da atividade *'
    )

    activity = models.ForeignKey(
        Activity,
        verbose_name=u'Atividade',
        help_text=u'Informe a atividade *'
    )

    priority = models.CharField(
        u'Prioridade',
        choices=OPTIONS,
        default=EASY,
        max_length=100,
        help_text=u'Informe uma prioridade *'
    )

    status = models.BooleanField(
        u'Finalizado',
        help_text=u'Marque apenas se a tarefa estiver finalizada'
    )

    class Meta:
        verbose_name=u'Tarefa'
        verbose_name_plural=u'Tarefas'
        ordering = ['-id']

    def __str__(self):
        return self.name
