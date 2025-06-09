from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Usuario(AbstractUser):
    """User model for the tracker app."""
    pass

class Serie(models.Model):
    TIPO_ANIME = 'ANIME'
    TIPO_MANGA = 'MANGA'
    TIPO_CHOICES = [
        (TIPO_ANIME, 'Anime'),
        (TIPO_MANGA, 'Mangá'),
    ]

    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=5, choices=TIPO_CHOICES)
    sinopse = models.TextField()
    total_eps_capitulos = models.PositiveIntegerField()
    em_lancamento = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.titulo

class Avaliacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avaliacoes')
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='avaliacoes')
    progressos = models.PositiveIntegerField(default=0)
    nota = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)

    class Meta:
        unique_together = ('usuario', 'serie')

    def __str__(self) -> str:
        return f"{self.usuario} - {self.serie} ({self.nota})"
