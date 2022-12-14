# Generated by Django 4.1.3 on 2022-11-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0005_pregunta_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('categoria', models.CharField(choices=[('CN', 'Ciencias'), ('MA', 'Matematicas'), ('LE', 'Lectura'), ('IN', 'Ingles'), ('SC', 'Sociales')], default='CN', max_length=2)),
                ('published', models.DateTimeField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('preguntas', models.ManyToManyField(to='preguntas.pregunta')),
            ],
        ),
    ]
