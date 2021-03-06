# Generated by Django 2.2.12 on 2020-05-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('cedula', models.CharField(max_length=10)),
                ('resenia', models.CharField(max_length=1400)),
                ('formal', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=140)),
                ('provincia', models.CharField(choices=[('sanjose', 'San Jose'), ('alajuela', 'Alajuela'), ('heredia', 'Heredia'), ('cartago', 'Cartago'), ('limon', 'Limón'), ('puntarenas', 'Puntarenas'), ('guanacaste', 'Guanacaste')], max_length=10)),
                ('canton', models.CharField(max_length=100)),
                ('distrito', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=140)),
            ],
        ),
    ]
