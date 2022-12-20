"""App configuration."""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Account configuration class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
