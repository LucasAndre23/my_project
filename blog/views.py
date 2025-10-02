from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime as date

# Create your views here.
def hello(request):
    return render(request, "blog.html")

def eco(request, param ):
    return HttpResponse(f"Você digitou {param}")

def api_info(request):
    data =  {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  }
    return JsonResponse(data)

def contato(request, nmr=40028922):
    return render (request, "contato.html", {"telefone": nmr})

def home(request):


    role = {
        "admin": "Administrador",
        "user": "Usuário Comum",
        
    }
    contexto = {
        "usuario": "Lucas",

        "valor": 100,
        "now": date.today(),
        "idade": 25,
        "is_logged_in": True,
        "user_role": "admin",
        "produtos": [
            {"nome": "Caneta", "preco": 1.50},
            {"nome": "Caderno", "preco": 15.00},
            {"nome": "Borracha", "preco": 0.80},
        ]
    }

    contexto["role"] = role[contexto["user_role"]]

    
    return render(request, "home.html", contexto)