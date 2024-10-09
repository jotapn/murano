# Generated by Django 5.1.1 on 2024-10-09 01:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacoes', '0011_alter_entrada_tipo_receita'),
        ('operacoes', '0003_delete_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='tipo_receita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receitas', to='operacoes.tiporeceita'),
        ),
    ]
