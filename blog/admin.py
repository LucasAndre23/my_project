from django.contrib import admin
from .models import Autor, Editora, Livro 
# Register your models here.




@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    
    list_display = ('nome',) 


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):

    list_display = ('nome',)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'ISBN', 'publicacao', 'estoque', 'editora')
    
    
    list_filter = ('editora', 'publicacao') 
    
    
    filter_horizontal = ('autores',)