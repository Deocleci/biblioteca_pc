from django.shortcuts import render
from livro.models import Livro
from user.models import CustomUser
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import ListView

class ListarUser(ListView):
    model = CustomUser
    template_name = 'livro/user.html'

    def get_queryset(self, **kwargs):
        cod = self.kwargs['codigo']
        qs = get_object_or_404(self.model, codigo=cod)
        return qs