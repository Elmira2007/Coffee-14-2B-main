# Generated by Django 5.0.1 on 2024-03-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Возраст пользователя')),
                ('subject', models.CharField(max_length=255, verbose_name='Вопроc пользователя')),
                ('message', models.TextField(verbose_name='Cообщения пользователя')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]