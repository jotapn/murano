# Generated by Django 5.1.1 on 2024-12-12 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_operacaofinanceira'),
    ]

    operations = [
        migrations.RenameField(
            model_name='naturezafinanceira',
            old_name='titulo',
            new_name='nome',
        ),
    ]
