# Generated by Django 2.0 on 2020-04-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField(verbose_name='descripcion')),
                ('image', models.ImageField(upload_to='projects', verbose_name='imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='fecha de edicion')),
            ],
            options={
                'verbose_name': 'blog',
                'ordering': ['-created'],
            },
        ),
    ]
