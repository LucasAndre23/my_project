from django import forms

from .models import Editora, Autor, Livro

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'ISBN', 'publicacao', 'preco', 'estoque', 'editora', 'autores']

