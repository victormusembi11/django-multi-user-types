"""Account models."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model."""

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
