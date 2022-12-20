"""Account model tests."""
import pytest

from accounts.models import Student, User

pytestmark = pytest.mark.django_db


def test_user_model_str(user: User):
    """Test model str."""
    assert str(user) == "johndoe"


def test_user_model_is_teacher(user: User):
    """Test is teacher boolean model field."""
    user.is_teacher = True
    assert user.is_teacher is True


def test_student_model_str(student: Student):
    """Test model str."""
    assert str(student) == "johndoe"


def test_user_model_is_student(student: Student):
    """Test is student boolean model field."""
    assert student.user.is_student is True
