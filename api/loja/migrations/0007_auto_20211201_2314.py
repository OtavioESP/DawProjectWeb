# Generated by Django 3.2.9 on 2021-12-01 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_usuario_hashtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='hashtag',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_criacao',
            field=models.DateField(auto_now_add=True),
        ),
    ]
