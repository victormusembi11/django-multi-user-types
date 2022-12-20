"""Account forms."""
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Student, User


class StudentSignupForm(UserCreationForm):
    """Generate student user account signup form."""

    class Meta(UserCreationForm.Meta):
        """Signup form meta."""

        model = User

    @transaction.atomic
    def save(self) -> User:
        """Save User object & create Student object."""
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)
        return user
