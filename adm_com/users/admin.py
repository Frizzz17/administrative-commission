from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Role, RoleUser


@admin.register(RoleUser)
class RoleUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'is_admin')


admin.site.register(User, UserAdmin)
admin.site.register(Role)
