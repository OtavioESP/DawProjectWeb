# Generated by Django 3.2.9 on 2021-11-29 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField()),
                ('texto', models.CharField(blank=True, max_length=500, null=True)),
                ('curtidas', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loja.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curtidas', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.post')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.usuario')),
            ],
        ),
    ]
