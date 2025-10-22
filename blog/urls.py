from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("eco/<str:param>/",views.eco),
    path("json",views.api_info),
    path("home/",views.home),
    path("contato/", views.contato),
    path('adicionar/', views.add_livro, name='add_livro'),
    path('',views.home, name='home'),
    path('livros/adicionar/', views.add_livro, name='add_livro'),
    path('livros/', views.list_livros, name='list_livros'),
    path('livros/edit/<int:livro_id>/', views.edit_livro, name='edit_livro')]