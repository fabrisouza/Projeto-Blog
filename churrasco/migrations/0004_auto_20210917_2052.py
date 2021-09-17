# Generated by Django 3.2.7 on 2021-09-17 20:52

import churrasco.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churrasco', '0003_auto_20210917_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, default=churrasco.models.randomString, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='churrasco',
            name='authorimage',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem do Autor'),
        ),
    ]