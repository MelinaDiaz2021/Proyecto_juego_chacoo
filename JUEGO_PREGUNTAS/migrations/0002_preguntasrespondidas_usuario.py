# Generated by Django 3.2.6 on 2021-08-21 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JUEGO_PREGUNTAS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='puntaje_total')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿es esta la respuesta correcta?')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='puntaje obtenido')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JUEGO_PREGUNTAS.pregunta')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='JUEGO_PREGUNTAS.elguirrespuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JUEGO_PREGUNTAS.usuario')),
            ],
        ),
    ]