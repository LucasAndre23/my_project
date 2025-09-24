from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def hello(request):
    return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, param ):
    return HttpResponse(f"Você digitou {param}")

def api_info(request):
    data =  {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  }
    return JsonResponse(data)

