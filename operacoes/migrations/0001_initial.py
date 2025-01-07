# Generated by Django 5.1.1 on 2025-01-07 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0007_alter_cadastro_cnpj_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroDeCusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('titulo', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('responsavel', models.ForeignKey(limit_choices_to={'atributos__tipo': 'CO'}, on_delete=django.db.models.deletion.PROTECT, to='cadastro.cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='NaturezaFinanceira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('titulo', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('ST', 'Sintética'), ('AN', 'Analítica')], max_length=2)),
                ('sinal', models.CharField(choices=[('CR', 'Crédito'), ('DB', 'Débito'), ('TR', 'Transitória')], max_length=2)),
                ('status', models.BooleanField(default=True)),
                ('grupo', models.ForeignKey(blank=True, limit_choices_to={'tipo': 'ST'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='operacoes.naturezafinanceira')),
            ],
            options={
                'verbose_name': 'Natureza Financeira',
                'verbose_name_plural': 'Naturezas Financeiras',
            },
        ),
    ]
