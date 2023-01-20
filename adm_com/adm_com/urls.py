from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
    path('', include('news.urls', namespace='news')),
]
