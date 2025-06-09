from django.contrib import admin

from .models import Serie, Avaliacao


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "em_lancamento")


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "serie", "nota", "progressos")
