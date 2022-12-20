"""Pytest fixtures."""
import pytest

from accounts.models import Student, User

pytestmark = pytest.mark.django_db


@pytest.fixture
def user() -> User:
    """User auth test fixture."""
    user = User.objects.create(username="johndoe", email="johndoe@example.com")
    user.set_password("john@123")
    return user


@pytest.fixture
def student(user: User) -> Student:
    """Student test fixture."""
    user.is_student = True
    return Student.objects.create(user=user)
