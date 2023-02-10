from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from users.views import NewUser, role_for_user, del_role_for_user


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
    ),
    path('role/', role_for_user, name='role'),
    path('role/del_role/', del_role_for_user, name='del_role')
]
