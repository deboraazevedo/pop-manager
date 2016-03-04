# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, error_messages={'unique': 'A user with that username already exists.'}, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('office', models.CharField(verbose_name='Cargo', max_length=100, help_text='Insira o cargo *', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'verbose_name': 'Pessoa',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nome', help_text='Insira o nome completo *', max_length=100)),
                ('description', models.TextField(verbose_name='Descrição', help_text='Insira a descrição da atividade *')),
                ('priority', models.CharField(default='Baixa', verbose_name='Prioridade', choices=[('Baixa', 'Baixa'), ('Normal', 'Normal'), ('Alta', 'Alta')], help_text='Informe uma prioridade *', max_length=100)),
                ('status', models.BooleanField(verbose_name='Finalizado', help_text='Marque apenas se a atividade estiver finalizada')),
            ],
            options={
                'verbose_name_plural': 'Atividades',
                'verbose_name': 'Atividade',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Diretoria', help_text='Insira uma diretoria *', max_length=100)),
                ('description', models.TextField(verbose_name='Descrição', help_text='Insira uma descrição *')),
            ],
            options={
                'verbose_name_plural': 'Diretorias',
                'verbose_name': 'Diretoria',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Gerência', help_text='Insira uma gerência *', max_length=100)),
                ('description', models.TextField(verbose_name='Descrição', help_text='Insira uma descrição *')),
            ],
            options={
                'verbose_name_plural': 'Gerências',
                'verbose_name': 'Gerência',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Título da tarefa', help_text='Insira um nome da tarefa *', max_length=100)),
                ('start_date', models.DateTimeField(verbose_name='Data de inicio', help_text='Insira a data de inicio *')),
                ('conclusion_date', models.DateTimeField(verbose_name='Data de conclusão', help_text='Insira a data de conclusão *')),
                ('description', models.TextField(verbose_name='Descrição', help_text='Insira uma descrição da atividade *')),
                ('priority', models.CharField(default='Baixa', verbose_name='Prioridade', choices=[('Baixa', 'Baixa'), ('Normal', 'Normal'), ('Alta', 'Alta')], help_text='Informe uma prioridade *', max_length=100)),
                ('status', models.BooleanField(verbose_name='Finalizado', help_text='Marque apenas se a tarefa estiver finalizada')),
                ('activity', models.ForeignKey(verbose_name='Atividade', to='core.Activity', help_text='Informe a atividade *')),
                ('people', models.ForeignKey(verbose_name='Responsável', to=settings.AUTH_USER_MODEL, help_text='Selecione uma pessoa para essa tarefa *')),
            ],
            options={
                'verbose_name_plural': 'Tarefas',
                'verbose_name': 'Tarefa',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='direction',
            name='management',
            field=models.ManyToManyField(to='core.Management', verbose_name='Gerêcias', help_text='Selecione as gerências *'),
        ),
        migrations.AddField(
            model_name='activity',
            name='management',
            field=models.ManyToManyField(to='core.Management', verbose_name='Gerêcias', help_text='Selecione as gerências *'),
        ),
        migrations.AddField(
            model_name='people',
            name='direction',
            field=models.ManyToManyField(to='core.Direction', verbose_name='Diretorias', help_text='Informe as diretorias *'),
        ),
        migrations.AddField(
            model_name='people',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', related_name='user_set', blank=True, to='auth.Group', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AddField(
            model_name='people',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', related_name='user_set', blank=True, to='auth.Permission', related_query_name='user', help_text='Specific permissions for this user.'),
        ),
    ]
