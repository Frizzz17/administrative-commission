from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import CreateUserForm


class NewUser(CreateView):
    '''Регестрирует нового пользователя.'''
    form_class = CreateUserForm
    success_url = reverse_lazy('news:index')
    template_name = 'users/reg_user.html'
    
    def get(self, request, *args, **kwargs):
        '''Проверяет является ли пользователь администратором и отдает get. '''
        self.object = None
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('users:login')

    def post(self, request, *args, **kwargs):
        '''Проверяет является ли пользователь администратором и отдает post. '''
        self.object = None
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        return redirect('users:login')