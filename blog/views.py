from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime as date
from .form import LivroForm
from django.shortcuts import redirect

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


def add_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_livros')  # Após salvar, redireciona para a lista de livros
    else:
        form = LivroForm()  
    return render(request, 'add_livro.html', {'form': form})


def list_livros(request):
    from .models import Livro
    livros = Livro.objects.all()
    return render(request, 'list_livros.html', {'livros': livros})

def edit_livro(request, livro_id):
    from .models import Livro
    livro = Livro.objects.get(id=livro_id)  # Obtemos o livro pelo ID
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('list_livros')  # Redireciona para a lista de livros após salvar
    else:
        form = LivroForm(instance=livro)  # Preenche o formulário com os dados do livro
    return render(request, 'edit_livro.html', {'form': form, 'livro': livro})
