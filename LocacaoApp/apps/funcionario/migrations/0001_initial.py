# Generated by Django 5.2.1 on 2025-06-17 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('cargo', models.CharField(max_length=50)),
                ('data_admissao', models.DateField()),
                ('email_corporativo', models.EmailField(max_length=254)),
            ],
        ),
    ]
