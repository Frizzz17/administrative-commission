from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from users import views


app_name = 'users'


urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path('new_user/', views.NewUser.as_view(), name='new_user'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('roles/<str:username>/', views.role_for_user, name='roles'),
    path(
        'roles/del_role/<str:username>',
        views.del_role_for_user,
        name='del_role'
    ),
    path('all_users/', views.get_all_users, name='all_users'),
    path('user/<str:username>/', views.user_info, name='userinfo')
]
