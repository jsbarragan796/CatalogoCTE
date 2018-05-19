# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_anterior', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('instrucciones', models.CharField(max_length=500)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('revisor1', models.IntegerField(blank=True, null=True)),
                ('revisor2', models.IntegerField(blank=True, null=True)),
                ('autor', models.IntegerField()),
                ('estado', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pendiente de Revisi\xf3n'), (2, 'Pendiente de Publicaci\xf3n'), (3, 'Publicado'), (4, 'Bloqueado'), (5, 'Hist\xf3rico'), (6, 'Borrador')], null=True)),
            ],
        ),
        migrations.CreateModel(

            name='CorreoConfiguracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lastSend', models.CharField(blank=True, max_length=500, null=True)),
                ('pending', models.PositiveSmallIntegerField(blank=True, null=True)),

            ],
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_anterior', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('urlReferencia', models.CharField(max_length=500)),
                ('sistemaOperativo', models.CharField(max_length=80)),
                ('plataforma', models.CharField(blank=True, max_length=50, null=True)),
                ('fichaTecnica', models.CharField(max_length=2000)),
                ('licencia', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=520)),
                ('logo', models.CharField(max_length=500)),
                ('revisor1', models.IntegerField(blank=True, null=True)),
                ('revisor2', models.IntegerField(blank=True, null=True)),
                ('autor', models.IntegerField()),
                ('estado', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pendiente de Revisi\xf3n'), (2, 'Pendiente de Publicaci\xf3n'), (3, 'Publicado'), (4, 'Bloqueado'), (5, 'Hist\xf3rico'), (6, 'Borrador')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotoUrl', models.CharField(blank=True, max_length=500, null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Administrador'), (2, 'Miembro GTI')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecursoActividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_anterior', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('funcionalidad', models.CharField(max_length=500)),
                ('revisor1', models.IntegerField(blank=True, null=True)),
                ('revisor2', models.IntegerField(blank=True, null=True)),
                ('autor', models.IntegerField()),
                ('estado', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pendiente de Revisi\xf3n'), (2, 'Pendiente de Publicaci\xf3n'), (3, 'Publicado'), (4, 'Bloqueado')], null=True)),
                ('herramienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Herramienta')),
            ],
        ),
        migrations.AddField(
            model_name='recursotutorial',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Tutorial'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='herramienta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Herramienta'),
        ),
    ]
