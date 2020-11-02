from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns = [
  path('', views.login_view, name='login'),

]
