from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core import management
from django.test import TestCase
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class TestCore(TestCase):
    valid_username = 'alice'
    valid_password = '1234'

    invalid_username = 'john'
    invalid_password = '12345'

    def get_token(self) -> dict:
        data = {
            'username': self.valid_username,
            'password': self.valid_password,
        }
        response = self.client.post(
            path=reverse('login'),
            data=data,
            format='json',
        )
        return response.json()

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        management.call_command('createadmin')
        management.call_command('seed')

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    @property
    def valid_user(self) -> User:
        return User.objects.get(username=self.valid_username)

    @property
    def valid_user_authorization_headers(self) -> dict:
        access_token = self.get_token()['access']
        return {
            'Authorization': f'Bearer {access_token}',
        }

    @property
    def invalid_user_authorization_headers(self) -> dict:

        class User:

            def __init__(self) -> None:
                self.id = str(uuid4())

        access_token = str(RefreshToken.for_user(user=User()).access_token)
        return {
            'Authorization': f'Bearer {access_token}',
        }
