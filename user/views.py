from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm


def index(request):
    return render(request, 'user/index.html')

class RegisterUser(CreateView):
    form_class = UserForm
    template_name = 'user/register.html'
    success_url = '/'

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')