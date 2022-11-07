from django.utils import timezone

from django.db import models
from django.utils.text import slugify

CIENCIAS = 'CN'
MATEMATICAS = 'MA'
LECTURA = 'LE'
INGLES = 'IN'
SOCIALES = 'SC'
PRUEBAS = [
    (CIENCIAS, 'Ciencias'),
    (MATEMATICAS, 'Matematicas'),
    (LECTURA, 'Lectura'),
    (INGLES, 'Ingles'),
    (SOCIALES, 'Sociales'),
]

class RespuestaMultiple(models.Model):
    texto = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.texto


class Pregunta(models.Model):
    categoria = models.CharField(
        max_length=2,
        choices=PRUEBAS,
        default=CIENCIAS,
        null=True,
        blank=True
    )
    contexto = models.TextField(null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    opciones = models.ManyToManyField(RespuestaMultiple)
    respuesta_correcta = models.ManyToManyField(RespuestaMultiple, related_name="correcta", blank=True)
    explicacion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.texto


class Quiz(models.Model):
    '''A quiz template'''
    #setter = models.ForeignKey(User, related_name='setter')
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(choices=PRUEBAS, default=CIENCIAS, max_length=2)
    preguntas = models.ManyToManyField(Pregunta)
    publicado = models.DateTimeField(blank=True, null=True)
    fecha_agregado = models.DateTimeField(default=timezone.now)
    fecha_modificado = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        fecha_slug = self.fecha_modificado.strftime('%Y-%m-%d')
        self.slug = slugify(self.titulo + ' ' + fecha_slug)
        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
