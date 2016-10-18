from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User


class UserAdmin(BaseUserAdmin):

    fieldsets = BaseUserAdmin.fieldsets

admin.site.register(User, UserAdmin)
