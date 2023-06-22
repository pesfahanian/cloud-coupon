from django.core import management
from django.test import TestCase
from django.urls import reverse


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
