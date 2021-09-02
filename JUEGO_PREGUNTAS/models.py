
from django.db import models
from django.db.models import aggregates
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.conf import settings

from django.contrib.auth.models import User

from django.db.models.fields.related import ForeignKey
import random

# Create your models here.
class Pregunta(models.Model):
    NUMERO_DE_RESPUESTAS_PERMITIDA = 2

    texto =models.TextField(verbose_name='texto de preguntas')
    max_puntaje=models.DecimalField(verbose_name='Maximo puntaje',default=3,decimal_places=2,max_digits=6)

    def __str__ (self):
        return self.texto

class ElguirRespuesta(models.Model):

    MAXIMO_RESPUESTAS=4

    preguntas=models.ForeignKey (Pregunta,on_delete=models.CASCADE,related_name= 'opciones')
    correcta=models.ForeignKey('Respuesta',on_delete=models.RESTRICT,related_name='responde a')
    texto=models.TextField(verbose_name= 'Texto de la respuesta')

    def __str__ (self):
        return self.texto

class Quizusuario(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.CASCADE)
    puntaje_total=models.DecimalField(verbose_name='puntaje_total',default=0,decimal_places=2,max_digits=10)
    
    def crear_intentos(self,pregunta):
        intento=PreguntasRespondidas(pregunta=pregunta,quizUser=self)
        intento.save()


    def obtener_nuevas_preguntas(self):
        respondidas=PreguntasRespondidas.objects.filter(quizUser=self).values_list('pregunta_pk',flat=True)
        preguntas_restantes= Pregunta.objectas.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)

    def validar_intento(self, pregunta_respondida, respuesta_selecionada):
        if respuesta_selecionada.correcto is True:
            pregunta_respondida.correcto=True
            pregunta_respondida.puntaje_obtenido=respuesta_selecionada.pregunta.max_puntaje
            pregunta_respondida.respusta=respuesta_selecionada

        else:
            pregunta_respondida.respuesta=respuesta_selecionada

        pregunta_respondida.save()

        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        puntaje_actualizado=self.intentos.filter(correcta=True).Aggregate(
            models.Sum('puntaje_obtenido'))['puntaje_obtenido_sum']

        self.puntaje_total=puntaje_actualizado
        self.save()

		
		
    

		


class PreguntasRespondidas(models.Model):
    quizuser=models.ForeignKey(Quizusuario,on_delete=models.CASCADE,related_name='intentos')
    pregunta=models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    respuesta=models.ForeignKey(ElguirRespuesta,on_delete=models.CASCADE,null=True)
    correcta=models.BooleanField(verbose_name='¿es esta la respuesta correcta?',default= False,null=False)
    puntaje_obtenido=models.DecimalField(verbose_name='puntaje obtenido',default=0,decimal_places=2,max_digits=6)
