# Generated by Django 3.2.9 on 2021-11-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='curtidas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='curtidas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
