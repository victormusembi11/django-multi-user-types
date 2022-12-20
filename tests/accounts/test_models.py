"""Account model tests."""
import pytest

from accounts.models import User

pytestmark = pytest.mark.django_db


def test_user_model_str(user: User):
    """Test model str."""
    assert str(user) == "johndoe"


def test_user_model_is_student(user: User):
    """Test is student boolean model field."""
    user.is_student = True
    assert user.is_student is True


def test_user_model_is_teacher(user: User):
    """Test is teacher boolean model field."""
    user.is_teacher = True
    assert user.is_teacher is True
