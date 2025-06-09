from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """Custom user model stored in the accounts app."""

    nome = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:  # pragma: no cover - representation
        return self.nome or self.username
