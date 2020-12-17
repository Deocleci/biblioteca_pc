from django.contrib import admin
from livro.models import Livro
from user.models import CustomUser
# Register your models here.
admin.site.register(Livro)
admin.site.register(CustomUser)