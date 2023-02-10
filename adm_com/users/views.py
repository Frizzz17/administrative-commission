from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import CreateUserForm, RoleForm


class NewUser(CreateView):
    '''Регестрирует нового пользователя.'''
    form_class = CreateUserForm
    success_url = reverse_lazy('users:role')
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
def role_for_user(request):
    '''Создаёт роль для действующего пользователя.'''
    template = 'users/role_for_user.html'

    form = RoleForm()

    if request.POST.get('role') is not None:
        roles.append(request.POST.get('role'))

    context = {
        'form': form,
        'roles': roles
    }

    return render(request, template_name=template, context=context)


@login_required
def del_role_for_user(request):
    '''Удаляет роль пользователя.'''
    roles.pop()
    print(roles)
    return redirect('users:role')
