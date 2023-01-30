from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Role, RoleUser


admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(RoleUser)