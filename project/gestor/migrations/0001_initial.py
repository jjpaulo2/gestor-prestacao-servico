# Generated by Django 3.1.7 on 2021-04-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone / Celular')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]