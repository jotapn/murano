# Generated by Django 5.1.1 on 2024-10-18 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operacoes', '0002_operacoes_xpto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operacoes',
            name='xpto',
        ),
    ]