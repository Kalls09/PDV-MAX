from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = Users

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'cargo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'cargo'),
        }),
    )

    list_display = ('username', 'email', 'cargo', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
