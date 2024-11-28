# Generated by Django 5.1.1 on 2024-11-14 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacoes', '0003_remove_operacoes_xpto'),
        ('transacoes', '0002_alter_transacao_options_categoria_classificacao_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'ordering': ['-data'], 'verbose_name': 'Transação', 'verbose_name_plural': 'Transações'},
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='status',
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='update_at',
        ),
        migrations.AddField(
            model_name='categoria',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='transacao',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Atualização'),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='metodo_pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transacao_metodo', to='operacoes.tipopagamento', verbose_name='Método Pagamento'),
        ),
    ]