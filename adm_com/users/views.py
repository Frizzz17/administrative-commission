from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import CreateUserForm, RoleForm
from users.models import User


class NewUser(CreateView):
    '''Регестрирует нового пользователя.'''
    form_class = CreateUserForm
    success_url = reverse_lazy('users:roles', kwargs={'username': 'andr'})
    template_name = 'users/reg_user.html'
    
    def get(self, request, *args, **kwargs):
        '''Проверяет является ли пользователь администратором и отдает get.'''
        self.object = None
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('users:login')

    def post(self, request, *args, **kwargs):
        '''Проверяет является ли пользователь администратором и отдает post.'''
        self.object = None
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        return redirect('users:login')

roles = []
@login_required
def role_for_user(request, username):
    '''Создаёт роль для действующего пользователя.'''
    template = 'users/role_for_user.html'

    user = User.objects.get(username=username)

    form = RoleForm()

    if request.POST.get('role') is not None:
        roles.append(request.POST.get('role'))

    context = {
        'form': form,
        'roles': roles,
        'user': user
    }

    return render(request, template_name=template, context=context)


@login_required
def del_role_for_user(request, username):
    '''Удаляет роль пользователя.'''
    roles.pop()
    print(roles)
    return redirect('users:roles', username)
