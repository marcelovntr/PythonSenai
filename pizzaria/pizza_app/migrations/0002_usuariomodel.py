# Generated by Django 5.1.6 on 2025-04-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=20)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
