from django.contrib.auth.forms import UserCreationForm
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