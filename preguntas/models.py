from django.db import models

class RespuestaMultiple(models.Model):
    texto = models.TextField()
    imagen = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.texto


class Pregunta(models.Model):
    contexto = models.CharField(max_length=200, null=True, blank=True)
    texto = models.CharField(max_length=200, null=True)
    opciones = models.ManyToManyField(RespuestaMultiple)
    respuesta_correcta = models.ManyToManyField(RespuestaMultiple, related_name="correcta", blank=True)
    explicacion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    # upload = models.ImageField(upload_to ='uploads/% Y/% m/% d/')

    def __str__(self):
        return self.texto

