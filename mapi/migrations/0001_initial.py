# Generated by Django 3.1.7 on 2021-03-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compradores',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('longitud', models.CharField(max_length=200)),
                ('latitud', models.CharField(max_length=200)),
                ('estado_geo', models.CharField(max_length=200)),
            ],
        ),
    ]