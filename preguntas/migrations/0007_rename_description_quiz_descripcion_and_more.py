# Generated by Django 4.1.3 on 2022-11-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0006_quiz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='date_added',
            new_name='fecha_agregado',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='date_modified',
            new_name='fecha_modificado',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='published',
        ),
        migrations.AddField(
            model_name='quiz',
            name='publicado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
