from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre = "JS", camada = 57783)
    curso.save()
    documento = f'Curso: {curso.nombre} - Camada: {curso.camada}'
    return HttpResponse(documento)

