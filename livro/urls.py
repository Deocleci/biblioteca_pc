from django.urls import path
from . import views
from user.views import ListarUser
from django.contrib.auth import views as auth_views

app_name = 'livro'

urlpatterns = [
  path('', views.index, name='index'),
  path('cadastrar/', views.Cadastrar.as_view(), name='cadastrar'),
  path('listar/', views.LivroList.as_view(), name='listar'),
  path('deletar/<int:pk>/', views.DeleteLivro.as_view(), name='delete'),
  path('editar/<int:pk>/', views.EditLivro.as_view(), name='editar'),
  path('pesquisar/', views.pesquisar, name='pesquisar'),
  path('listaruser/<codigo>', ListarUser.as_view(), name='listUser'),

]
