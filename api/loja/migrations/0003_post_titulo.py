# Generated by Django 3.2.9 on 2021-11-29 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20211129_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
