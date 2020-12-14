from django.db import models
from django.contrib.auth.models import AbstractUser #User

# Create your models here.
class CustomUser(AbstractUser):
  is_admin = models.BooleanField('administrador', default=False)
  codigo = models.CharField(max_length=16)
  is_admin = models.BooleanField('administrador', default=False)
  email = models.EmailField(('email address'), unique=True,        error_messages={
            'unique': ("Email já existe."),
        },)
  REQUIRED_FIELDS = ['email', 'is_admin']
  username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text= ('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': ("Usuario já existe."),
        },
    )
  class Meta:
    verbose_name = "Cliente"
    verbose_name_plural = "Clientes"

  def __str__(self):
    return self.first_name if self.first_name is not None else self.username