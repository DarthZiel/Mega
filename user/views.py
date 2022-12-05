from django.urls import reverse_lazy
from django.views.generic import CreateView

from Mega.user.forms import UserForm


class RegisterUser(CreateView):
    form_class = UserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

