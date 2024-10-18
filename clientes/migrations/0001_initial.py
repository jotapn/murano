# Generated by Django 5.1.1 on 2024-10-18 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xpto', models.CharField(max_length=1)),
                ('nome_fantasia', models.CharField(max_length=80)),
                ('razao_social', models.CharField(max_length=80)),
                ('tipo_pessoa', models.CharField(blank=True, choices=[('pf', 'Pessoa física'), ('pj', 'Pessoa jurídica')], max_length=20, null=True)),
                ('cnpj_cpf', models.CharField(max_length=18)),
                ('cep', models.CharField(max_length=9)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=6)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]
