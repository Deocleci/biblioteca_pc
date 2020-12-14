from django.shortcuts import render
from livro.models import  Livro
from livro.forms import LivroForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

def index(request):

    return render(request, 'livro/index.html', {})


class Cadastrar(CreateView):
    """
    View para a criação de novos livros.
    """
    model = Livro
    form_class = LivroForm
    template_name = 'livro/cadastrar.html'
    success_url = reverse_lazy('livro:listar')

class LivroList(ListView):
    """
    View para listar veiculos livros.
    """
    model = Livro
    template_name = 'livro/listar.html'

class DeleteLivro(DeleteView):
    """
    View para a exclusão de livro.
    """
    model = Livro
    template_name = 'livro/deletar.html'
    success_url = reverse_lazy('livro:listar')


class EditLivro(UpdateView):
    """
    View para a edição de veiculos.
    """
    model = Livro
    form_class = LivroForm
    template_name = 'livro/editar.html'
    success_url = reverse_lazy('livro:listar')


def pesquisar(request):
    if request.method == 'POST':
        return redirect("/index/listaruser/" + request.POST['codigo'] )
    return render(request, "livro/pesquisarUser.html", {})

