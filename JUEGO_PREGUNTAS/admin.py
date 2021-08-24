from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline
from django.db import models


from .models import Pregunta ,ElguirRespuesta,PreguntasRespondidas,Quizusuario

from.forms import EleguirInlineFormset

class EleguirRespuestasInline(admin.TabularInline):

    model=ElguirRespuesta
    can_delete=False
    max_num=ElguirRespuesta.MAXIMO_RESPUESTAS
    min_num=ElguirRespuesta.MAXIMO_RESPUESTAS
    formset=EleguirInlineFormset

class PreguntasAdmin(admin.ModelAdmin):
    model=Pregunta 

    inlines=(EleguirRespuestasInline, )
    list_display=['texto',]
    search_fields=['texto','preguntas_texto']



class PreguntasRespondidasAdmin(admin.ModelAdmin):
      list_display=['pregunta','respuesta','correcta','puntaje_obtenido']

      class Meta:
          model=PreguntasRespondidas

admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta,PreguntasAdmin)
admin.site .register (ElguirRespuesta)
admin.site .register (Quizusuario)
