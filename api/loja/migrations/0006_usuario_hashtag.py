# Generated by Django 3.2.9 on 2021-12-01 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_comentario_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='hashtag',
            field=models.CharField(default='@', max_length=30),
        ),
    ]
