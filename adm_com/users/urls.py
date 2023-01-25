from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from users.views import NewUser


app_name = 'users'


urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path('new_user/', NewUser.as_view(), name='new_user'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    )
]