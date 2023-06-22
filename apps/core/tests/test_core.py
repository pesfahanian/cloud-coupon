from uuid import uuid4

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import management
from django.test import TestCase
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken

from apps.wallet.models import Wallet

settings.DEBUG = True

User = get_user_model()


class TestCore(TestCase):
    valid_username = 'alice'
    valid_password = '1234'

    invalid_username = 'john'
    invalid_password = '12345'

    invalid_code = 'AAAAA*'
    invalid_coupon_type = -1
    invalid_server = -1

    def get_token(self) -> dict:
        data = {
            'username': self.valid_username,
            'password': self.valid_password,
        }
        return self.client.post(
            path=reverse('login'),
            data=data,
            format='json',
        )

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
    def valid_user_wallet(self) -> Wallet:
        return Wallet.objects.get(user=self.valid_user)

    @property
    def valid_user_authorization_headers(self) -> dict:
        access_token = self.get_token().json()['access']
        return {
            'Authorization': f'Bearer {access_token}',
        }

    @property
    def invalid_user_authorization_headers(self) -> dict:

        class _User:

            def __init__(self) -> None:
                self.id = str(uuid4())

        access_token = str(RefreshToken.for_user(user=_User()).access_token)
        return {
            'Authorization': f'Bearer {access_token}',
        }

    @property
    def _valid_user_authorization_headers(self) -> dict:

        class _User:

            def __init__(self) -> None:
                self.id = str(User.objects.get(username='bob').id)

        access_token = str(RefreshToken.for_user(user=_User()).access_token)
        return {
            'Authorization': f'Bearer {access_token}',
        }
