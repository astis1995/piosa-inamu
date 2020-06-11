# Generated by Django 2.2.12 on 2020-06-03 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('appimagenes', '0007_auto_20200602_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='appimagenes_imagenesmodel', serialize=False, to='cms.CMSPlugin')),
                ('nombre', models.CharField(max_length=140)),
                ('cedula', models.CharField(max_length=10)),
                ('foto_de_perfil', models.BooleanField(default=False)),
                ('foto_de_producto', models.BooleanField(default=False)),
                ('imagen', models.ImageField(upload_to='imagenes/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='appimagenes_persona', serialize=False, to='cms.CMSPlugin')),
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
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
