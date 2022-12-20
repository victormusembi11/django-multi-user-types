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


class TeacherSignupForm(UserCreationForm):
    """Generate teacher user account signup form."""

    class Meta(UserCreationForm.Meta):
        """Signup form meta."""

        model = User

    def save(self, commit=True) -> User:
        """Set user is teacher attribute to True then save."""
        user: User = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user
