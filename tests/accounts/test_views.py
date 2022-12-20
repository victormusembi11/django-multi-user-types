"""Test account views."""
import pytest
from django.test import Client

from accounts.models import Student

pytestmark = pytest.mark.django_db


def test_student_signup_view(client: Client):
    """Test success GET request."""
    response = client.get('/accounts/signup/student/')
    assert response.status_code == 200


def test_student_signup_success(client: Client):
    """Test success POST request."""
    response = client.post(
        '/accounts/signup/student/',
        data={
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'john@123',
            'password2': 'john@123'
        }
    )
    assert response.status_code == 302


def test_student_dahboard(client: Client, student: Student):
    """Test success GET request."""
    client.login(username="johndoe", password="john@123")
    response = client.get('/accounts/student/dashboard/')
    assert response.status_code == 200


def test_teacher_signup_view(client: Client):
    """Test success GET response."""
    response = client.get('/accounts/signup/teacher/')
    assert response.status_code == 200


def test_teacher_signup_success(client: Client):
    """Test success POST request."""
    response = client.post(
        '/accounts/signup/teacher/',
        data={
            'username': 'janedoe',
            'email': 'janedoe@example.com',
            'password1': 'jane@123',
            'password2': 'jane@123'
        }
    )
    assert response.status_code == 302
