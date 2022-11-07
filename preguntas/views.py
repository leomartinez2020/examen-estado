from django.shortcuts import render

from .models import Pregunta, RespuestaMultiple

def index(request):
    preguntas = Pregunta.objects.all()
    context = {'preguntas': preguntas}
    return render(request, 'preguntas/main.html', context)
