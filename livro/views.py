from django.shortcuts import render
from livro.models import  Livro
from livro.forms import LivroForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import  TemplateView
from django.views import View

from livro.models import Livro
from user.models import CustomUser

from django.shortcuts import render, get_object_or_404



# def index(request):
#
#     return render(request, 'livro/index.html', {})

def admin_check(user):
  return user.is_admin





@method_decorator(login_required, name='dispatch')
class Index(TemplateView):
    template_name = 'livro/index.html'

    # def dispatch(self, request, *args, **kwargs):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livroemprestado'] = Livro.objects.filter(emprestado=True).count()
        context['livrodisponiveis'] = Livro.objects.filter(emprestado=False).count()
        context['usucomlivro'] = CustomUser.objects.filter(livro__emprestado=True).count()
        context['userativo'] = CustomUser.objects.filter(is_active=True).count()
        return context

@method_decorator(login_required,  name='dispatch')
class Cadastrar(CreateView):
    """
    View para a criação de novos livros.
    """
    model = Livro
    form_class = LivroForm
    template_name = 'livro/cadastrar.html'
    success_url = reverse_lazy('livro:listar')

@method_decorator(login_required, name='dispatch')
class LivroList(ListView):
    """
    View para listar veiculos livros.
    """
    model = Livro
    template_name = 'livro/listar.html'
    
@method_decorator(login_required, name='dispatch')
class DeleteLivro(DeleteView):
    """
    View para a exclusão de livro.
    """
    model = Livro
    template_name = 'livro/deletar.html'
    success_url = reverse_lazy('livro:listar')

@method_decorator(login_required, name='dispatch')
class EditLivro(UpdateView):
    """
    View para a edição de veiculos.
    """
    model = Livro
    form_class = LivroForm
    template_name = 'livro/editar.html'
    success_url = reverse_lazy('livro:listar')

@login_required
def pesquisar(request):
    if request.method == 'POST':
        return redirect("/index/listaruser/" + request.POST['codigo'] )
    return render(request, "livro/pesquisarUser.html", {})

@method_decorator(login_required, name='dispatch')
class Emprestar(TemplateView):
    template_name = 'livro/avisoOK.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        livro = self.kwargs['livro']
        print(request.POST['codigo'] )
        print(self.kwargs['livro'] )
        user = get_object_or_404(CustomUser, codigo= request.POST['codigo'] )
        livro = get_object_or_404(Livro, id=livro)
        if  livro in user.livro_set.all() or livro.emprestado:
            return redirect('livro:aviso', "Livro Emprestado")
        livro.user = user
        livro.emprestado = True
        livro.save()
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class Aviso(TemplateView):
    template_name = 'livro/aviso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aviso'] = self.kwargs['aviso']
        return context

@method_decorator(login_required, name='dispatch')
class Devolver(View):

    def dispatch(self, request, *args, **kwargs):
        livro = self.kwargs['livro']
        livroObject = get_object_or_404(Livro, id=livro)
        livroObject.emprestado = False
        print(livroObject.user.id)
        livroObject.user_id = ""
        livroObject.save()
        return redirect('livro:aviso', "Livro Devolvido")
        return super().dispatch(request, *args, **kwargs)

