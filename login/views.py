from django.shortcuts import render
from login.forms import LoginForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse

# def login_view(request):
#
#     return render(request, 'login/login.html', {})



def login_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            # Redirect to a success page.
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('livro:index'))

            return render(request, 'login/login.html', {'form': form, 'mensage': 'Incorrect username or password.'})

    else:
        form = LoginForm()
    return  render(request, 'login/login.html', {'form': form})

