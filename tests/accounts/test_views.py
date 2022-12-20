"""Test account views."""
import pytest
from django.test import Client

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
