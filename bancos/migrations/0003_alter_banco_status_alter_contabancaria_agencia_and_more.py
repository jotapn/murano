# Generated by Django 5.1.1 on 2024-11-14 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancos', '0002_remove_banco_xpto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='status',
            field=models.CharField(choices=[('AT', 'Ativo'), ('IN', 'Inativo')], default='AT', max_length=2),
        ),
        migrations.AlterField(
            model_name='contabancaria',
            name='agencia',
            field=models.CharField(max_length=20, verbose_name='Agência'),
        ),
        migrations.AlterField(
            model_name='contabancaria',
            name='status',
            field=models.CharField(choices=[('AT', 'Ativo'), ('IN', 'Inativo')], default='AT', max_length=2),
        ),
    ]
