# Generated by Django 3.2.6 on 2021-08-23 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JUEGO_PREGUNTAS', '0003_auto_20210823_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntasrespondidas',
            old_name='usuario',
            new_name='quizuser',
        ),
    ]
