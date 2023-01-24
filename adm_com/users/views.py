from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import CreateUserForm


class NewUser(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('news:index')
    template_name = 'users/reg_user.html'
