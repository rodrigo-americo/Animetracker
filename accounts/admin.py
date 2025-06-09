from django.contrib import admin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "email",
        "last_login",
        "created_at",
        "updated_at",
    )
