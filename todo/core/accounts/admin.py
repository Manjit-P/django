from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreation, CustomUserChange, CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    list_display = (
        'username',
        'email',
        'age',
    )

    fieldsets = UserAdmin.fieldsets + ((None, {'fields':("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':("age",)}),)

admin.site.register(CustomUser, CustomUserAdmin)