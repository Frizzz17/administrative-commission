from django.contrib.auth.forms import UserCreationForm
from django import forms
from news.models import User


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'username',
            'position'
        )


class RoleForm(forms.Form):
    role = forms.ChoiceField(
        choices=[
            (1, 'Председатель'),
            (2, 'Член комиссии')
        ],
        label='Роль'
    )
